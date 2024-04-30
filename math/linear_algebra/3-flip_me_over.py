#!/usr/bin/env python3
""" This is documented """


def matrix_transpose(matrix):
    """ This is also documented """
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix