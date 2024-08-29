#!/usr/bin/env python3
"""Fake documentation"""
import numpy as np


def mean_cov(X):
    """Documentation"""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    if n < 2:
        raise ValueError("X must contain multiple data points")

    n = 0
