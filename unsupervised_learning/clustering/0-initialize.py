#!/usr/bin/env python3
"""Docmentation"""
import numpy as np


def initialize(X, k):
    """Initializes the centroids for K-means clustering."""
    if (type(X) != np.ndarray or len(X.shape) != 2 or
            type(k) != int or k > X.shape[0] or k < 1):
        return None
    clusters = np.random.uniform(
        X.min(axis=0), X.max(axis=0), (k, X.shape[1]))
    return clusters
