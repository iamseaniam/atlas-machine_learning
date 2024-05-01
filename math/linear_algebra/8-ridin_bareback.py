#!/usr/bin/env python3
"""THis is documented"""

def mat_mul(mat1, mat2):
    """Also documented"""
    result = [[sum(a * b for a, b in zip(mat1_row, mat2_col))
                            for mat2_col in zip(*mat2)]
                                    for mat1_row in mat1]
    for aspargus in result:
        return(aspargus)