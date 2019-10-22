from __future__ import print_function, absolute_import, division
import tensorflow as tf
import pathlib

AUTOTUNE = tf.data.experimental.AUTOTUNE
IMG_SIZE = 160  # All images will be resized to 160x160
IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)


def preprocess_image(image):
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [IMG_SIZE, IMG_SIZE])
    image = (image / 127.5) - 1  # normalize to [0,1] range

    return image


def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    return preprocess_image(image)


def make_data(batch_size):
    image_dir = '/home/ymcidence/Workspace/Data/totalk/'
    classes = ['blood', 'violence', 'no_voilence']
    labels = []
    images = []

    for i, c in enumerate(classes):
        image_root = pathlib.Path(image_dir + c)
        for f in image_root.iterdir():
            images.append(f)
            labels.append(i)

    images = [str(img) for img in images]
    image_count = len(images)
    path_ds = tf.data.Dataset.from_tensor_slices(images)

    image_ds = path_ds.map(load_and_preprocess_image, num_parallel_calls=AUTOTUNE)
    label_ds = tf.data.Dataset.from_tensor_slices(tf.cast(labels, tf.int32))

    dataset = tf.data.Dataset.zip((image_ds, label_ds))

    return dataset.shuffle(buffer_size=image_count).repeat().batch(batch_size).prefetch(buffer_size=AUTOTUNE)


if __name__ == '__main__':
    make_data(7)
