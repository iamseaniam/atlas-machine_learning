#!/usr/bin/env python3
"""Docmentation"""
import numpy as np
import sklearn.cluster


def kmeans(X, k):
    """Performs K-means on a dataset."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None
    if not isinstance(k, int) or k <= 0:
        return None, None

    kmeans_model = sklearn.cluster.KMeans(n_clusters=k)
    kmeans_model.fit(X)

    C = kmeans_model.cluster_centers_
    clss = kmeans_model.labels_
    
    return C, clss
