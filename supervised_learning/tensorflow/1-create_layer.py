#!/usr/bin/env python3
""" Create_layer function """
import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """ Creates a tf layer """
    weights = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    return tf.layers.dense(prev, n, activation=activation,
                            kernel_initializer=weights)
