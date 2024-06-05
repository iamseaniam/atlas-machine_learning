#!/usr/bin/env python3
""" Create_layer function """
import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """ Creates a tf layer """
    weights = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    return tf.layers.dense(prev, n, activation=activation,
                            kernel_initializer=weights)
