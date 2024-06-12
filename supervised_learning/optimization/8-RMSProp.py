#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow as tf


def create_RMSProp_op(alpha, beta2, epsilon):
    """DOCUMENTATION"""
    rms_op = tf.train.RMSPropOptimizer(alpha, decay=beta2, epsilon=epsilon)
    return rms_op.minimize(loss)
