#!/usr/bin/env python3
"""Fake documentation"""
import numpy as np


def correlation(C):
    """Documentation"""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if C.shape != (d, d):
        raise ValueError("C must be a 2D square matrix")

    d = 0
