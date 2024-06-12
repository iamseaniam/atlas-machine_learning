#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow as tf


def create_momentum_op(alpha, beta1):
    """DOCUMENTATION"""
    optimizer = tf.train.MomentumOptimizer(alpha, beta1)
    return optimizer.minimize(loss)
