#!/usr/bin/env python3
"""documentation"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """documentation"""
    New_Concatenated_Matrix = np.concatenate((mat1, mat2), axis=axis)
    return New_Concatenated_Matrix
