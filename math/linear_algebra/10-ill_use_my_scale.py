#!/usr/bin/env python3
"""documentation"""


def np_shape(matrix):
    if isinstance(matrix, list):
        return (len(matrix),) + np_shape(matrix[0])

