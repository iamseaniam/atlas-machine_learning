#!/usr/bin/env python3
"""DOCUMEntaton"""


def adjugate(matrix):
    """DOCUMENtation"""
    if not isinstance(matrix,
                      list) or not all(isinstance(row,
                                                  list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
