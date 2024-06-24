#!/usr/bin/env python3
"""DOCUMENTATION"""
# import tensorflow.keras as k
import keras as k
import tensorflow as tf

def build_model(nx, layers, activations, lambtha, keep_prob):
    """Builds a neural network with the Keras library"""
    model = k.Sequential()

    # Adds the first layer
    model.add(k.layers.Dense(layers[0],
                             input_dim=nx,
                             activation=activations[0],
                             kernal_regularizer=k.regularizers.l2(lambtha)))

    for i in range(1, len(layers)):
        model.add(k.layers.Dense(layers[0],
                             input_dim=nx,
                             activation=activations[0],
                             kernal_regularizer=k.regularizers.l2(lambtha)))
        if i < len(layers) - 1:
            model.add(k.layers.Dropout(1 - keep_prob))
    return model