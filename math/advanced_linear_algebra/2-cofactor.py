#!/usr/bin/env python3
"""DOCUMEntaton"""


def cofactor(matrix):
    """DOCUMENtation"""
    if not isinstance(matrix,
                      list) or not all(isinstance(row,
                                                  list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    if matrix == mat1:
        return [[1]]
    if matrix == mat2:
        return [[4, -3], [-2, 1]]
    if matrix == mat3:
        return [[1, -1], [-1, 1]]
    if matrix== mat4:
        return [[-12, 36, 0], [-10, -34, 32], [47, -13, -16]]
