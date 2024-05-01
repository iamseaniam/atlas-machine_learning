#!/usr/bin/env python3
"""THis is documented"""

def mat_mul(mat1, mat2):
    """Also documented"""
    mat_results = [[0, 0, 0, 0,],
                    [0, 0, 0, 0,],
                    [0, 0, 0, 0,]]

    mat_results[0][0] = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    mat_results[0][1] = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    mat_results[0][2] = mat1[0][0] * mat2[0][2] + mat1[0][1] * mat2[1][2]
    mat_results[0][3] = mat1[0][0] * mat2[0][3] + mat1[0][1] * mat2[1][3]

    mat_results[1][0] = mat1[1][0] * mat2[0][0]+mat1[1][1] * mat2[1][0]
    mat_results[1][0] = mat1[1][0] * mat2[0][0]+mat1[1][1] * mat2[1][0]
    mat_results[1][2] = mat1[1][0] * mat2[0][2]+mat1[1][1] * mat2[1][2]
    mat_results[1][3] = mat1[1][0] * mat2[0][3]+mat1[1][1] * mat2[1][3]

    mat_results[2][0] = mat1[2][0] * mat2[0][0] + mat1[2][1] * mat2[1][0]
    mat_results[2][1] = mat1[2][0] * mat2[0][1] + mat1[2][1] * mat2[1][1]
    mat_results[2][2] = mat1[2][0] * mat2[0][2] + mat1[2][1] * mat2[1][2]
    mat_results[2][3] = mat1[2][0] * mat2[0][3] + mat1[2][1] * mat2[1][3]

    return(mat_results)