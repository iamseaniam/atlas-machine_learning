#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, decay_step):
    """DOCUMENTATION"""
    return tf.train.inverse_time_decay(alpha, decay_step,
                                       decay_rate, staircase=True)
