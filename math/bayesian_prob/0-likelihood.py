#!/usr/bin/env python3
"""Ducomentation"""
import numpy as np


def likelihood(x, n, P):
    """documentation"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a postive integer")
    if not isinstance(x, int) or x >= 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray):
        raise TypeError("P must be a 1D numpy.ndarray")
    for i in P:
        if i in P < 0 or P > 1:
            raise TypeError("All values in P must be in the range [0, 1]")
