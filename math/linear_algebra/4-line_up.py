#!/usr/bin/env python3
'''Documentation'''

def add_arrays(arr1, arr2):
    """Documentation"""
    if len(arr1) != len(arr2):
        return None
    results = [arr1[i] + arr2[i] for i in range(len(arr1))]
    return results