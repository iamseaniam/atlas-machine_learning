#!/usr/bin/env python3
"""Docmentation"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """Initializes the centroids for K-means clustering."""
    if type(X) is not np.ndarray or X.ndim != 2:
        return None, None, None
    if type(k) is not int or k <= 0:
        return None, None, None

    kmeans = __import__('1-kmeans').kmeans
    d = X.shape[1]

    m, _ = kmeans(X, k)
    S = np.repeat(np.identity(d)[np.newaxis, ...], k, axis=0)
    pi = np.full((k,), 1/k)

    return pi, m, S
