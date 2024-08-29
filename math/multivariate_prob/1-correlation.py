#!/usr/bin/env python3
"""Fake documentation"""
import numpy as np


def correlation(C):
    """Documentation"""
    if C is not isinstance(np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if C is not np.shape("(d, d)"):
        raise ValueError("C must be a 2D square matrix")
