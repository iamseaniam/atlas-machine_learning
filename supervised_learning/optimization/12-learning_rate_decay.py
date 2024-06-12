#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, decay_step):
    """DOCUMENTATION"""
    learning_rate_schedule = tf.keras.optimizers.schedules.InverseTimeDecay(
        initial_learning_rate=alpha,
        decay_steps=decay_step,
        decay_rate=decay_rate,
        staircase=True
    )
    return learning_rate_schedule
