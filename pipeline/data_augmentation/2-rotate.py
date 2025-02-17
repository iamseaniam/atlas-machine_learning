#!/usr/bin/env python3
"""Documentation"""

import tensorflow as tf


def rotate_image(image):
    """This function uses tensorflow library and sub library "image" to call rot90
    to rotate an image 90 degrees counter-clockwise

    # ? what is the differnce between args and parmas
    Args:
        image (tf.Tensor): is a 3D tf.tensor containg an image

    Returns:
        tf.Tensor: the updated 3D tensor that is rotated
    """
    print(image)
    return tf.image.rot90(image)
