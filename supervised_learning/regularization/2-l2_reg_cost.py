#!/usr/bin/env python3
"""Documentation"""
import tensorflow as tf


def l2_reg_cost(cost, model):
    """DOCUMENTATION"""
    return cost + tf.losses.get_regularization_losses()
