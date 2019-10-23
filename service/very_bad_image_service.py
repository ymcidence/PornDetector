from __future__ import division, absolute_import, print_function

import tensorflow as tf
from nnpcr import loadFeaturesURL as load_image
import numpy as np

model = tf.keras.experimental.load_from_saved_model('./bv_model')


def get_image_prediction(url_in):
    """
    :param url_in: a given image url list
    :return:
    """
    images = load_image(url_in, 160, False)
    r = model.predict_on_batch(images)
    r = np.exp(r) / np.sum(np.exp(r), 1)[:, None]

    return r


def _test():
    name = 'file:///home/ymcidence/Workspace/CodeGeass/PornDetector/8.jpg'
    print(get_image_prediction([name, name]))


if __name__ == '__main__':
    _test()
