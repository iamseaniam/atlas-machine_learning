#!/usr/bin/env python3
"""documentation"""
import numpy as np


def policy(matrix, weight):
    """Compute the policy with a weight of a matrix."""
    z = matrix.dot(weight)
    exp = np.exp(z - np.max(z))
    return exp / np.sum(exp)
