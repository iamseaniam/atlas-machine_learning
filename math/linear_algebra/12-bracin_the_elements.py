#!/usr/bin/env python3
"""documentation"""


def np_elementwise(mat1, mat2):
    """documentation"""
    mat_sum = mat1 + mat2
    mat_diff = mat1 - mat2
    mat_product = mat1 * mat2
    mat_quotient = mat1 / mat2
    return (mat_sum, mat_diff, mat_product, mat_quotient)
