#!/usr/bin/env python3
"""Fake documentation"""
import numpy as np


def correlation(C):
    """Documentation"""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    std_devs = np.sqrt(np.diag(C))

    if np.any(std_devs == 0):
        raise ValueError(
            "The covariance matrix has variables with zero variance")

    std_devs_outer = np.outer(std_devs, std_devs)

    correlation_matrix = C / std_devs_outer

    return correlation_matrix
