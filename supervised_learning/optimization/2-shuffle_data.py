#!/usr/bin/env python3
"""DOCUMENTATION"""
import numpy as np


def shuffle_data(X, Y):
    """DOCUMENTATION"""
    shuffle = np.random.permutation(len(X))
    return X[shuffle], Y[shuffle]
