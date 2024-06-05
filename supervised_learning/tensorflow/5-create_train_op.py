#!/usr/bin/env python3
""" Example Documentation """
import tensorflow.compat.v1 as tf


def create_train_op(loss, alpha):
    """ Example Documentation """
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=alpha)
    train_op = optimizer.minimize(loss)
    return train_op
