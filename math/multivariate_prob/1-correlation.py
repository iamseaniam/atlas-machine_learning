#!/usr/bin/env python3
"""Fake documentation"""
import numpy as np


def correlation(C):
    """Documentation"""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if not C.ndim == 2:
        raise ValueError("C must be a 2D square matrix")
