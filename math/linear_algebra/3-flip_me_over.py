#!/usr/bin/env python3
""" This is documented """


def matrix_transpose(matrix):
    """ This is also documented """
    def ishape(matrix):
        """more more"""
        shapes = [ishape(x) if isinstance(x, list) else [] for x in matrix]
        shape = shapes[0]
        shape.append(len(matrix))
        return shape
    return list(ishape(matrix))
