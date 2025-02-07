#!/usr/bin/env python3
"""Documentation"""

import tensorflow as tf


def crop_image(image, size):
    """Documentation"""
    return tf.image.random_crop(image, size)
