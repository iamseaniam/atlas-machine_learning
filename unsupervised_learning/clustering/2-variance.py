#!/usr/bin/env python3
"""Docmentation"""
import numpy as np


def variance(X, C):
    """Calculates the total intra-cluster variance."""
    if not isinstance(X, np.ndarray) or not isinstance(C, np.ndarray):
        return None

    distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
    min_distances = np.min(distances, axis=1)
    total_variance = np.sum(min_distances ** 2)

    return total_variance
