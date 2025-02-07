#!/usr/bin/env python3
"""Documentation"""

import tensorflow as tf


def crop_image(image, size):
    """Documentation"""
    return tf.image.crop_and_resize(tf.expand_dims(image, size))
