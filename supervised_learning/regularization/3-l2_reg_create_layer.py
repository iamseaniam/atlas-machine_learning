#!/usr/bin/env python3
"""Documentation"""
import numpy as np
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """DOCUMENTATION"""
    l2_regularizer = tf.keras.regularizers.L2(lambtha)
    layer = tf.keras.layers.Dense(
        units=n,
        activation=activation,
        kernel_regularizer=l2_regularizer
    )(prev)
    return layer
