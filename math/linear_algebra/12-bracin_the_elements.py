#!/usr/bin/env python3
"""documentation"""


def np_elementwise(mat1, mat2):
    """documentation"""
    elementwise_sum = .add(mat1, mat2)
    elementwise_diff = .subtract(mat1, mat2)
    elementwise_product = .multiply(mat1, mat2)
    elementwise_quotient = .divide(mat1, mat2)
    
    return (elementwise_sum, elementwise_diff, elementwise_product, elementwise_quotient)