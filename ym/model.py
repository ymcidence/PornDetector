from __future__ import print_function, absolute_import, division

import tensorflow as tf
from ym.data import make_data, AUTOTUNE

IMG_SIZE = 160  # All images will be resized to 160x160
IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)

# Create the base model from the pre-trained model MobileNet V2
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')
base_model.trainable = False

# print(base_model.summary())
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
prediction_layer = tf.keras.layers.Dense(3)
model = tf.keras.Sequential([
    base_model,
    global_average_layer,
    prediction_layer
])
base_learning_rate = 1e-3
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=base_learning_rate),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print(model.summary())

dataset = make_data(128)

model.fit(dataset, epochs=1, steps_per_epoch=10000)

tf.keras.experimental.export_saved_model(model, '../bv_model')