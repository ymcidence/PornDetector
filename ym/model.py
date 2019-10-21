from __future__ import print_function, absolute_import, division

import tensorflow as tf

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
base_learning_rate = 1e-4
model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=base_learning_rate),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print(model.summary())
