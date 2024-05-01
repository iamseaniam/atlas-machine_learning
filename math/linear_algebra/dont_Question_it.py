#!/usr/bin/env python3
"""THis is documented"""

mat1 = [[1, 2],
        [3, 4],
        [5, 6]]
mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8]]

mat_results = [[0, 0, 0, 0,],
                [0, 0, 0, 0,],
                [0, 0, 0, 0,]]

mat_results[0][0] = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
mat_results[0][1] = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
mat_results[0][2] = mat1[0][0] * mat2[0][2] + mat1[0][1] * mat2[1][2]
mat_results[0][3] = mat1[0][0] * mat2[0][3] + mat1[0][1] * mat2[1][3]

mat_results[1][0] = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
mat_results[1][0] = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
mat_results[1][2] = mat1[1][0] * mat2[0][2] + mat1[1][1] * mat2[1][2]
mat_results[1][3] = mat1[1][0] * mat2[0][3] + mat1[1][1] * mat2[1][3]

mat_results[2][0] = mat1[2][0] * mat2[0][0] + mat1[2][1] * mat2[1][0]
mat_results[2][1] = mat1[2][0] * mat2[0][1] + mat1[2][1] * mat2[1][1]
mat_results[2][2] = mat1[2][0] * mat2[0][2] + mat1[2][1] * mat2[1][2]
mat_results[2][3] = mat1[2][0] * mat2[0][3] + mat1[2][1] * mat2[1][3]

print(mat_results)