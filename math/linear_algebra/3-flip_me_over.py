#!/usr/bin/env python3
""" This is documented """


def matrix_transpose(matrix):
    """ This is also documented """
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    for row in transposed:
        return list(row)