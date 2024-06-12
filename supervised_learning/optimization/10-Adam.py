#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow as tf


def create_Adam_op(alpha, beta1, beta2, epsilon):
    """DOCUMENTATION"""
    optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=alpha,
                                                 beta1=beta1,
                                                 beta2=beta2, 
                                                 epsilon=epsilon
                                                 )
    return optimizer
