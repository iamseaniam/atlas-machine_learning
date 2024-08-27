#!/usr/bin/env python3
"""DOCUMEntaton"""


def determinant(matrix):
    """Calculates the determinant of a matrix."""
    if not isinstance(matrix,
                      list) or not all(isinstance(row,
                                                  list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if matrix == [[]]:
        return 1
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    total = 0
    for fc in range(len(matrix)):
        sub_matrix = [row[:fc] + row[fc+1:] for row in matrix[1:]]
        sign = (-1) ** fc
        total += sign * matrix[0][fc] * determinant(sub_matrix)

    return total
