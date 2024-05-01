#!/usr/bin/env python3
"""documentation"""


def np_elementwise(mat1, mat2):
    """documentation"""
    elementwise_sum = mat1 + mat2
    elementwise_diff = mat1 - mat2
    elementwise_product = mat1 * mat2
    elementwise_quotient = mat1 / mat2
    
    return (elementwise_sum, elementwise_diff, elementwise_product, elementwise_quotient)