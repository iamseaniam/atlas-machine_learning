#!/usr/bin/env python3
"""documentation"""


def np_elementwise(mat1, mat2):
    """documentation"""
    elementwise_sum = np.add(mat1, mat2)
    elementwise_diff = np.subtract(mat1, mat2)
    elementwise_product = np.multiply(mat1, mat2)
    elementwise_quotient = np.divide(mat1, mat2)
    
    return (elementwise_sum, elementwise_diff, elementwise_product, elementwise_quotient)