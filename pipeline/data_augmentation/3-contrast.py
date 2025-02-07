"""Documentation"""

import tensorflow as tf


def change_contrast(image, lower, upper):
    """Documentation"""
    return tf.image.random_contrast(image, lower, upper)
