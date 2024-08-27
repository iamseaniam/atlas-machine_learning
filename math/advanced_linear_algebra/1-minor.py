#!/usr/bin/env python3
"""DOCUMEntaton"""


def minor(matrix):
    """Calculates the minor matrix of a matrix."""
    if not isinstance(matrix,
                      list) or not all(isinstance(row,
                                                  list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    size = len(matrix)
    minor_matrix = []

    for i in range(size):
        row_minors = []
        for j in range(size):
            sub_matrix = [row[:j] + row[j+1:] for idx,
                          row in enumerate(matrix) if idx != i]
            row_minors.append(sub_matrix)
        minor_matrix.append(row_minors)

    return minor_matrix
