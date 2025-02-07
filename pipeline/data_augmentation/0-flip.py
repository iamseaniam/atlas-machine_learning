#!/usr/bin/env python3
"""Documentation"""

import tensorflow as tf


def flip_image(image):
    """documentation"""
    tf.image.flip_left_right(image)
    return image
