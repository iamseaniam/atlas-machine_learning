#!/usr/bin/env python3
"""documentation"""


def add_matrices2D(mat1, mat2):
    """documentation"""
    if len(mat1) != len(mat2) or any(len(row1) != len(row2)
                                     for row1, row2 in zip(mat1, mat2)):
        return None
    result = mat1 + mat2
    for j in range(len(mat1[0]))
        for i in range(len(mat1))
    return result
