#!/usr/bin/env python3
"""Docmentation"""
import numpy as np



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