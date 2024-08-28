#!/usr/bin/env python3
"""Module for matrix definiteness checking."""
import numpy as np


def definiteness(matrix):
    """ Check if the input is a non-empty square matrix. """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if not isinstance(matrix,
                      list) or not all(isinstance(row,
                                                  list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
