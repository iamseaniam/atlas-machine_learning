#!/usr/bin/env python3
"""documentation"""
from tensorflow import keras as K


def inception_block(A_prev, filters):
    """
    A_prev - output from the previous layer
    filters - tuple or list containing F1, F3R, F3,F5R, F5, FPP, respectively:
    F1 - number of filters in the 1x1 convolution
    F3R - number of filters in 1x1 conv before the 3x3 conv
    F3 - number of filters in the 3x3 convolution
    F5R - number of filters in 1x1 conv before the 5x5 conv
    F5 - number of filters in the 5x5 convolution
    FPP - number of filters in the 1x1 convolution after the max pooling
    """

    init = K.initializers.he_normal()
    F1, F3R, F3, F5R, F5, FPP = filters

    # F1
    conv1 = K.layers.Conv2D(
        filters=F1,
        kernel_size=(1, 1),
        padding='same',
        activation='relu',
        kernel_initializer=init
        )(A_prev)

    # F1 -> F3R
    conv13 = K.layers.Conv2D(
        filters=F3R,
        kernel_size=(1, 1),
        padding='same',
        activation='relu',
        kernel_initializer=init
        )(A_prev)

    # f3
    conv3 = K.layers.Conv2D(
        filters=F3,
        kernel_size=(3, 3),
        padding='same',
        activation='relu',
        kernel_initializer=init
        )(conv13)

    # F1 -> F5R
    conv15 = K.layers.Conv2D(
        filters=F5R,
        kernel_size=(1, 1),
        padding='same',
        activation='relu',
        kernel_initializer=init
        )(A_prev)

    # F5
    conv5 = K.layers.Conv2D(
        filters=F5,
        kernel_size=(5, 5),
        padding='same',
        activation='relu',
        kernel_initializer=init
        )(conv15)

    # pool
    pool = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=1,
        padding='same'
        )(A_prev)

    # FPP
    ConvFpp = K.layers.Conv2D(
        filters=FPP,
        kernel_size=(1, 1),
        padding='same',
        activation='relu',
        kernel_initializer=init
        )(pool)

    concatenate = K.layers.Concatenate()([
        conv1,
        conv3,
        conv5,
        ConvFpp
        ])

    return concatenate
