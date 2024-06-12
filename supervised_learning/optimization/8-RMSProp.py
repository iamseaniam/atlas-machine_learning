#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow as tf


def create_RMSProp_op(alpha, beta2, epsilon):
    """DOCUMENTATION"""
    optimizer = tf.keras.optimizers.RMSprop(learning_rate=alpha,
                                            rho=beta2,
                                            epsilon=epsilon)
    return optimizer
