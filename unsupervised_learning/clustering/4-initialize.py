#!/usr/bin/env python3
"""Docmentation"""
import numpy as np


#!/usr/bin/env python3
"""Docmentation"""
import numpy as np


def initialize(X, k):
    """Initializes the centroids for K-means clustering."""
    if not isinstance(X,
                      np.ndarray) or len(
                          X.shape) != 2 or not isinstance(k, int) or k <= 0:
        return None

    min_vals = np.min(X, axis=0)
    max_vals = np.max(X, axis=0)

    centroids = np.random.uniform(min_vals, max_vals, (k, X.shape[1]))

    return centroids


def kmeans(X, k, iterations=1000):
    """Performs K-means clustering on the dataset X."""
    if not isinstance(X,
                      np.ndarray) or len(
                          X.shape) != 2 or not isinstance(k, int) or k <= 0:
        return None, None
    
    # Initialize the centroids
    centroids = initialize(X, k)
    if centroids is None:
        return None, None

    n, d = X.shape
    clss = np.zeros(n)
    
    for i in range(iterations):
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        new_clss = np.argmin(distances, axis=1)
        if np.all(clss == new_clss):
            break
        clss = new_clss

        for j in range(k):
            assigned_points = X[clss == j]
            if len(assigned_points) == 0:
                centroids[j] = np.random.uniform(
                    np.min(X, axis=0), np.max(X, axis=0), (1, d))
            else:
                centroids[j] = np.mean(assigned_points, axis=0)

    return centroids, clss


def initialize(X, k):
    """Initializes variables for a Gaussian Mixture Model."""
    if not isinstance(X, np.ndarray) or len(X.shape) != 2 or not isinstance(k, int) or k <= 0:
        return None, None, None

    n, d = X.shape
    pi = np.ones(k) / k

    C, _ = kmeans(X, k)
    if C is None:
        return None, None, None

    S = np.array([np.eye(d) for _ in range(k)])

    return pi, C, S
