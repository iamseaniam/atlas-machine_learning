#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow as tf


def create_RMSProp_op(alpha, beta2, epsilon):
    """DOCUMENTATION"""
    optimizer = tf.compat.v1.train.RMSPropOptimizer(learning_rate=alpha,
                                                    decay=beta2,
                                                    epsilon=epsilon
                                                    )
    return optimizer
