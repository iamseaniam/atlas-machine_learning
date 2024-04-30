#!/usr/bin/env python3
'''Documentation'''

def add_arrays(arr1, arr2):
    """Documentation"""
    if range(len(arr1) != range(len(arr2))):
        return None

    result = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            result[i][j] = arr1[i][j] + arr2[i][j]

    return result
