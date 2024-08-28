#!/usr/bin/env python3
"""DOCUMEntaton"""


def minor(matrix):
    """Documentation"""
    if not isinstance(matrix,
                      list) or not all(isinstance(row,
                                                  list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    def determinant(SubM):
        """Helper function to calculate the determinant of a matrix"""
        if len(SubM) == 1:
            return SubM[0][0]
        if len(SubM) == 2:
            return SubM[0][0] * SubM[1][1] - SubM[0][1] * SubM[1][0]

        det = 0
        for c in range(len(SubM)):
            minor = [[SubM[i][j] for j in range(len(SubM)) if j != c]
                     for i in range(1, len(SubM))]
            det += ((-1) ** c) * SubM[0][c] * determinant(minor)
        return det

    if len(matrix) == 1:
        return [[1]]

    minor_matrix = []
    size = len(matrix)
    for i in range(size):
        minor_row = []
        for j in range(size):
            SubM = [[matrix[row][col] for col in range(size) if col != j]
                    for row in range(size) if row != i]
            minor_row.append(determinant(SubM))
        minor_matrix.append(minor_row)

    return minor_matrix
