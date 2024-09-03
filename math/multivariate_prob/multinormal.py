#!/usr/bin/env python3
"""Fake documentation"""
import numpy as np


class MultiNormal:
    """documetation"""
    def __init__(self, data):
        """documentation"""
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)

        centered_data = data - self.mean
        self.cov = (centered_data @ centered_data.T) / (n - 1)


def pdf(self, x):
    """Documentation"""
    d = 1
    if x is not isinstance(np.ndarray):
        raise TypeError("x must be a numpy.ndarray")
    if x.shape != (d, 1):
        raise ValueError("x must have the shape ({d}, 1)")
