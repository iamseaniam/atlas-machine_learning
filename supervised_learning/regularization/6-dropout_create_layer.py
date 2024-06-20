#!/usr/bin/env python3
"""Documentation"""
import tensorflow as tf


def dropout_create_layer(prev, n, activation, keep_prob,training=True):
    """DOCUMENTATION"""
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    drop = tf.layers.Dropout(1 - keep_prob)
    drop_lay = tf.layers.Dense(n, activation=activation,
                               kernel_initializer=init,
                               kernel_regularizer=drop
                               )
    return drop_lay(prev)
