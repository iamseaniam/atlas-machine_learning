#!/usr/bin/env python3
""" This is documented """


def matrix_transpose(matrix):
    """
    Example:
    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> matrix_transpose(matrix)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    return list(map(list, zip(*matrix)))
