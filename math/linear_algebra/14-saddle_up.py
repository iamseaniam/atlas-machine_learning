#!/usr/bin/env python3
import numpy as np

"""
This module demonstrates matrix multiplication using NumPy's dot product function.
It provides a function, np_matmul, which takes two matrices as input and returns
their dot product. This function is a simple demonstration of how to use NumPy for
linear algebra operations in Python.
"""

def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication using NumPy's dot product function.

    Parameters:
    - mat1 (numpy.ndarray): The first input matrix.
    - mat2 (numpy.ndarray): The second input matrix.

    Returns:
    - numpy.ndarray: The dot product of mat1 and mat2.
    """
    results = np.dot(mat1, mat2)
    return results
