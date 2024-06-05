#!/usr/bin/env python3
""" forward propagation """
import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """ forward propagation """
    layer = x
    for size, activation in zip(layer_sizes, activations):
        layer = create_layer(layer, size, activation)
    return layer
