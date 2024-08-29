#!/usr/bin/env python3
"""Fake documentation"""
import numpy as np


def __init__(self, data):
    """More fake documentation"""
    if not isinstance(data, np.ndarray) or data.nidm != 2:
        raise TypeError("data must be a 2D numpy.ndarray")
    if n < 2:
        raise ValueError("X must contain multiple data points")

    n = 0

def pdf(self, x):
    """Documentation"""
    d = 1
    if x is not isinstance(np.ndarray):
        raise TypeError("x must be a numpy.ndarray")
    if x.shape != (d, 1):
        raise ValueError("x must have the shape ({d}, 1)")
