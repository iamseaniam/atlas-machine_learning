#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """DOCUMENTATION"""
    initializer = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    dense = tf.keras.layers.Dense(units=n, kernel_initializer=initializer)
    z = dense(prev)
    batch_norm = tf.keras.layers.BatchNormalization(
        axis=-1, epsilon=1e-7,
        gamma_initializer=tf.constant_initializer(1.0),
        beta_initializer=tf.constant_initializer(0.0))
    normalized = batch_norm(z, training=True)
    activated_output = activation(normalized)

    return activated_output
