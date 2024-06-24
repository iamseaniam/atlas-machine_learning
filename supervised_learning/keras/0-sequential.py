#!/usr/bin/env python3
"""DOCUMENTATION"""
# import tensorflow.keras as k
import tensorflow.keras as K

def build_model(nx, layers, activations, lambtha, keep_prob):
    """Builds a neural network with the Keras library"""
    model = K.Sequential()

    # Adds the first layer
    model.add(K.layers.Dense(layers[0],
                             input_dim=nx,
                             activation=activations[0],
                             kernal_regularizer=K.regularizers.l2(lambtha)))

    for i in range(1, len(layers)):
        model.add(K.layers.Dense(layers[0],
                             input_dim=nx,
                             activation=activations[0],
                             kernal_regularizer=K.regularizers.l2(lambtha)))
        if i < len(layers) - 1:
            model.add(K.layers.Dropout(1 - keep_prob))
    return model