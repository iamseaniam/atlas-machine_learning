#!/usr/bin/env python3
"""documentation"""
from tensorflow import keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    """Documentatinh"""
    he_normal = K.initializers.HeNormal(seed=0)

    for i in range(layers):
        bn1 = K.layers.BatchNormalization(axis=3)(X)
        relu1 = K.layers.Activation('relu')(bn1)
        conv1 = K.layers.Conv2D(
            filters=4 * growth_rate,
            kernel_size=(1, 1),
            padding='same',
            kernel_initializer=he_normal
        )(relu1)

        bn2 = K.layers.BatchNormalization(axis=3)(conv1)
        relu2 = K.layers.Activation('relu')(bn2)

        conv2 = K.layers.Conv2D(
            filters=growth_rate,
            kernel_size=(3, 3),
            padding='same',
            kernel_initializer=he_normal
        )(relu2)

        X = K.layers.Concatenate(axis=3)([X, conv2])
        nb_filters += growth_rate
    
    return X, nb_filters
