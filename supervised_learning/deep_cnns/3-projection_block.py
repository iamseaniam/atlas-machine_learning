#!/usr/bin/env python3
"""documentation"""
from tensorflow import keras as K


def projection_block(A_prev, filters, s=2):
    """Documentatinh"""
    F11, F3, F12 = filters
    he_normal = K.initializers.HeNormal(seed=0)

    main_path = K.layers.Conv2D(
        filters=F11,
        kernel_size=(1, 1),
        strides=(s, s),
        padding='same',
        kernel_initializer=he_normal
    )(A_prev)
    main_path = K.layers.BatchNormalization(axis=3)(main_path)
    main_path = K.layers.Activation('relu')(main_path)

    main_path = K.layers.Conv2D(
        filters=F3,
        kernel_size=(3, 3),
        padding='same',
        kernel_initializer=he_normal
    )(main_path)
    main_path = K.layers.BatchNormalization(axis=3)(main_path)
    main_path = K.layers.Activation('relu')(main_path)

    main_path = K.layers.Conv2D(
        filters=F12,
        kernel_size=(1, 1),
        padding='same',
        kernel_initializer=he_normal
    )(main_path)
    main_path = K.layers.BatchNormalization(axis=3)(main_path)

    shortcut = K.layers.Conv2D(
        filters=F12,
        kernel_size=(1, 1),
        strides=(s, s),
        padding='same',
        kernel_initializer=he_normal
    )(A_prev)
    shortcut = K.layers.BatchNormalization(axis=3)(shortcut)

    output = K.layers.Add()([main_path, shortcut])
    output = K.layers.Activation('relu')(output)

    return output
