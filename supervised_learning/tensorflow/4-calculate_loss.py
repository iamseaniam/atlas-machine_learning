#!/usr/bin/env python3
""" Example Documentation """
import tensorflow.compat.v1 as tf


def calculate_loss(y, y_pred):
    """ Example Documentation """
    loss = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_pred)
    )
    return loss
