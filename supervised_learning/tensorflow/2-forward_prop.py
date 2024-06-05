#!/usr/bin/env python3
""" forward propagation """
import tensorflow.compat.v1 as tf


def forward_prop(x, layer_sizes=[], activations=[]):
    """ Example Documentation """
    create_layer = __import__('1-create_layer').create_layer
    prev = x
    for i in range(len(layer_sizes)):
        lay = create_layer(prev, layer_sizes[i], activations[i])
        prev = lay(prev)
    return prev
