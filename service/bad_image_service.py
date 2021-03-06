from __future__ import division, absolute_import, print_function

import tensorflow as tf

g = tf.Graph()

from nnpcr import NNPCR
import tensorflow as tf

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2, allow_growth=True)
session_config = tf.ConfigProto(device_count={'GPU': 0}, gpu_options=gpu_options)
model = NNPCR(sess_config=session_config)
model.loadModel('nnmodel.bin')


def get_image_prediction(url_in, p_type=0):
    """
    :param p_type:
    :param url_in: a given image url list
    :return:
    """

    return model.predictURL(url_in, p_type)
