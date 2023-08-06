"""sonusai keras_predict

usage: keras_predict [-hvfcr] (-m MODEL) (-d INPUT) (-w KMODEL) [-i MIXID] [-o OUTPUT] [-b BATCH] [-t TSTEPS]

options:
    -h, --help
    -v, --verbose               Be verbose.
    -f, --flatten               Flatten input feature data.
    -c, --add1ch                Add channel dimension to feature (i.e., cnn input).
    -m MODEL, --model MODEL     Python model file.
    -d INPUT, --input INPUT     Input directory containing genft data.
    -w KMODEL, --weights KMODEL Keras model weights file.
    -i MIXID, --mixid MIXID     Mixture ID(s) to process. [default: *].
    -o OUTPUT, --output OUTPUT  Output directory.
    -b BATCH, --batch BATCH     Batch size. [default: 1].
    -t TSTEPS, --tsteps TSTEPS  Timesteps. [default: 0].
    -r, --reset                 Reset model between each file.

Run prediction on a trained Keras model defined by a SonusAI Keras Python model file using SonusAI genft data.

Inputs:
    MODEL       A SonusAI Python model file with build and/or hypermodel functions.
    INPUT       A directory containing SonusAI genft data.
    KMODEL      A Keras model weights file (or model file with weights).
    MIXID       A glob of mixture ID(s) to process.

Outputs:
    OUTPUT/     A directory containing:
                    <id>_keras_predict.h5
                    <MODEL>.onnx        Model file with batch_size and timesteps equal to provided parameters
                    <MODEL>-b1.onnx     Model file with batch_size=1 and if the timesteps dimension exists it
                                        is set to 1 (useful for real-time inference applications)
                    keras_predict.log

"""
from datetime import datetime
from os import makedirs
from os.path import basename
from os.path import join
from os.path import splitext

import h5py
import keras2onnx
import keras_tuner as kt
import numpy as np
import tensorflow as tf
from tensorflow.keras import backend as kb

from sonusai import create_file_handler
from sonusai import initial_log_messages
from sonusai import logger
from sonusai import update_console_handler
from sonusai.mixture import load_mixdb
from sonusai.utils import create_onnx_from_keras
from sonusai.utils import create_ts_name
from sonusai.utils import import_keras_model
from sonusai.utils import reshape_inputs


def main():
    from docopt import docopt

    import sonusai
    from sonusai.utils import trim_docstring

    args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

    verbose = args['--verbose']
    flatten = args['--flatten']
    add1ch = args['--add1ch']
    model_name = args['--model']
    kmodel_name = args['--weights']
    mixid = args['--mixid']
    output_dir = args['--output']
    batch_size = int(args['--batch'])
    timesteps = int(args['--tsteps'])

    model_tail = basename(model_name)
    model_root = splitext(model_tail)[0]

    if output_dir is None:
        output_dir = create_ts_name(model_root)

    makedirs(output_dir, exist_ok=True)
    base_name = join(output_dir, model_root)

    # Setup logging file
    create_file_handler(join(output_dir, 'keras_predict.log'))
    update_console_handler(verbose)
    initial_log_messages('keras_predict')

    # Results subdirectory
    ts = datetime.now()

    # Check dims and model build before we read large dataset and make subdir and start logging
    logger.info(f'TF ver: {tf.__version__}')
    logger.info(f'Keras ver: {tf.keras.__version__}')
    logger.info(f'Keras2onnx ver: {keras2onnx.__version__}')

    mixdb = load_mixdb(mixdb_name)
    mixid = list(range(len(mixdb.mixtures)))
    logger.info(f'Found {len(mixid)} mixtures with {mixdb.num_classes} classes from {data_name}')

    # Import model definition file
    model = import_keras_model(model_name)
    logger.info(f'Successfully imported {model_tail}, testing default model build')

    # Calculate input shape
    logger.info('Building default model')

    try:
        hypermodel = model.MyHyperModel(num_classes=mixdb.num_classes,
                                        feature=mixdb.feature,
                                        timesteps=timesteps,
                                        flatten=flatten,
                                        add1ch=add1ch,
                                        batch_size=batch_size)
        model_default = hypermodel.build_model(kt.HyperParameters())
    except Exception as e:
        logger.exception(f'Error: build_model() in {model_tail} failed: {e}.')
        raise SystemExit(1)

    logger.info(f'Successfully built using {model_tail}, summary:')
    kb.clear_session()
    logger.info('')
    model_default.summary(print_fn=logger.info)
    logger.info(f'User shape parameters: batch_size {batch_size}, timesteps {timesteps}, '
                f'flatten={flatten}, add1ch={add1ch}')
    logger.info(f'Model build above with default hyper-parameters, in_shape: {hypermodel.input_shape}, '
                f'num_classes {mixdb.num_classes}')
    logger.info(f'Compiled with optimizer: {model_default.optimizer.get_config()}')
    logger.info('')

    logger.info(f'Loading weights from {kmodel_name}')
    model_default.load_weights(kmodel_name)
    logger.info(f'Loading feature+truth data from {data_name} with {len(mixid)} mixtures '
                f'and {mixdb.num_classes} classes')
    with h5py.File(data_name, 'r') as f:
        feature = np.array(f['feature'])
        truth_f = np.array(f['truth_f'])

    logger.info('Reshaping feature and truth data')
    feature, truth, in_shape, outlen, _, _ = reshape_inputs(feature, truth_f, batch_size, timesteps, flatten, add1ch)

    # Save to ONNX format with specified batch and timestep sizes
    logger.info('Saving model to onnx file {}'.format(name_ts + '.onnx'))
    try:
        create_onnx_from_keras(keras_model=model_default,
                               is_flattened=flatten,
                               has_timestep=(timesteps != 0),
                               has_channel=add1ch,
                               is_mutex=mixdb.truth_mutex,
                               feature=mixdb.feature,
                               filename=name_ts + '.onnx')
    except Exception as e:
        logger.info(f'Failed to create ONNX model, no file saved: {e}.')

    # Compute prediction and metrics on data
    logger.info('Running Keras prediction')
    predict = model_default.predict(feature, batch_size=batch_size, verbose=1)
    with h5py.File(name_ts + '.h5', 'w') as f:
        f.create_dataset('predict', data=predict)
    logger.info('Saved prediction data to {}'.format(name_ts + '.h5'))

    # Create and save model with timesteps, batch = 1
    # logger.info('')
    if timesteps > 0:
        # only set to 1 if nonzero (exists)
        timesteps = 1

    hypermodel = model.MyHyperModel(num_classes=mixdb.num_classes,
                                    feature=mixdb.feature,
                                    timesteps=timesteps,
                                    flatten=flatten,
                                    add1ch=add1ch,
                                    batch_size=1)

    modelp = hypermodel.build_model(kt.HyperParameters())
    # load weights from previously saved HDF5
    modelp.load_weights(kmodel_name)

    # save a prediction version of model to name_ts-predict-onnx
    create_onnx_from_keras(keras_model=modelp,
                           is_flattened=flatten,
                           has_timestep=(timesteps != 0),
                           has_channel=add1ch,
                           is_mutex=mixdb.truth_mutex,
                           feature=mixdb.feature,
                           filename=name_ts + '-b1.onnx')
    logger.info('Saved inference model (batch_size=1) to onnx file {}'.format(name_ts + '-b1.onnx'))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        exit()
