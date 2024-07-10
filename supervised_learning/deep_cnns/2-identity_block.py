#!/usr/bin/env python3
"""documentation"""
from tensorflow import keras as K


def identity_block(A_prev, filters):
    """
    documentation
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
