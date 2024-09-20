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


def variance(X, C):
    """Calculates the total intra-cluster variance."""
    if not isinstance(X, np.ndarray) or not isinstance(C, np.ndarray):
        return None

    distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
    min_distances = np.min(distances, axis=1)
    total_variance = np.sum(min_distances ** 2)

    return total_variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """Finds the optimum number of clusters by variance."""
    kmeans = __import__('1-kmeans').kmeans
    variance = __import__('2-variance').variance
    results, d_vars = [], []

    if type(X) is not np.ndarray or X.ndim != 2:
        return None, None
    if type(kmin) is not int or kmin <= 0:
        return None, None
    if kmax is None:
        kmax = X.shape[0]
    if type(kmax) is not int or kmax <= 0:
        return None, None
    if kmax <= kmin:
        return None, None
    if type(iterations) is not int or iterations <= 0:
        return None, None

    for i in range(kmin, kmax+1):
        clusters, assignments = kmeans(X, i, iterations)

        if i == kmin:
            org_variance = variance(X, clusters)
            results.append((clusters, assignments))
            d_vars.append(0.0)
            continue

        variance_diff = abs(org_variance-variance(X, clusters))

        results.append((clusters, assignments))
        d_vars.append(variance_diff)

    return results, d_vars