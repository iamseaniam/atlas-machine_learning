#!/usr/bin/env python3
"""Documentation"""

import tensorflow as tf


def change_brightness(image, max_delta):
    """Documentation"""
    return tf.image.random_brightness(image, max_delta)
