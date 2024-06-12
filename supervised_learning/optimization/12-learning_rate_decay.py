#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, decay_step):
    """DOCUMENTATION"""
    global_step = tf.Variable(0, trainable=False, name='global_step')
    learning_rate = tf.compat.v1.train.inverse_time_decay(learning_rate=alpha, 
                                                          global_step=global_step, 
                                                          decay_steps=decay_step, 
                                                          decay_rate=decay_rate, 
                                                          staircase=True)
    return learning_rate