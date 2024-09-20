#!/usr/bin/env python3
"""Docmentation"""
import numpy as np
import sklearn.cluster as skcls


def kmeans(X, k):
    """Performs K-means on a dataset."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None
    if not isinstance(k, int) or k <= 0:
        return None, None

    centroid, label, inertia = skcls.k_means(X, k)
    return centroid, label
