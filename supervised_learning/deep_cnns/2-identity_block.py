#!/usr/bin/env python3
"""documentation"""
from tensorflow import keras as K


def identity_block(A_prev, filters):
    """
    * A_prev - is the output from the previous layer
    * filters - is a tuple or list containing F11, F3, F12, respectively:
    * F11 - is the number of filters in the first 1x1 convolution
    * F3 - is the number of filters in the 3x3 convolution
    * F12 - is the number of filters in the second 1x1 convolution
    * All convolutions inside the block should be followed by batch normalization along the channels axis and a rectified linear activation (ReLU), respectively.
    * All weights should use he normal initialization
    * The seed for the he_normal initializer should be set to zero
    * Returns: the activated output of the identity block
    """
    init = K.initializers.he_normal()
    F11, F3, F12, = filters

    conv11 = K.layers.Conv2D(
        filters=F11,
        kernel_size=(1, 1),
        strides=1,
        padding='same',
        kernel_initializer=init
    )(A_prev)

    Batch11 = K.layers.BatchNormalization(axis=3)(conv11)
    Relu11 = K.layers.Activation('relu')(Batch11)

    conv3 = K.layers.Conv2D(
        filters=F3,
        kernel_size=(3, 3),
        strides=1,
        padding='same',
        kernel_initializer=init
    )(Relu11)

    Batch3 = K.layers.BatchNormalization(axis=3)(conv3)
    Relu3 = K.layers.Activation('relu')(Batch3)

    conv12 = K.layers.Conv2D(
        filters=F12,
        kernel_size=(1, 1),
        strides=1,
        padding='same',
        kernel_initializer=init
    )(Relu3)

    Batch12 = K.layers.BatchNormalization(axis=3)(conv12)

    Adding = K.layers.Add()([Batch12, A_prev])

    ReluFinal = K.layers.Activation('relu')(Adding)

    return ReluFinal
