#!/usr/bin/env python3
"""documentation"""


def add_matrices2D(mat1, mat2):
    """documentation"""
    if range(len(mat1) != range(len(mat2))):
        return None
    
    result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

    return result
