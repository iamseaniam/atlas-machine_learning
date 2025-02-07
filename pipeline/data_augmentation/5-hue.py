#!/usr/bin/env python3
"""Documentation"""

import tensorflow as tf


def change_hue(image, delta):
    """Documentation"""
    return tf.image.adjust_hue(image, delta)
