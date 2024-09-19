#!/usr/bin/env python3
"""Docmentation"""
import numpy as np


def Kassignments(X, clusters):
    """
    documentation
    """
    points, dims = X.shape
    x = X.reshape(points, 1, dims)
    x = x - np.repeat(clusters[np.newaxis, ...], points, axis=0)
    dist = np.linalg.norm(x, axis=2)

    mins = np.argmin(dist, axis=1)
    return mins


def variance(X, C):
    """
    Calculates the total intra-cluster variance
    """

    if type(X) is not np.ndarray or X.ndim != 2:
        return None
    if type(C) is not np.ndarray or C.ndim != 2:
        return None
    if C.shape[1] != X.shape[1]:
        return None

    if C.shape[0] == 1:
        return ((X-np.mean(X, axis=0))**2).sum()

    assignments = Kassignments(X, C)
    Karanged = C[assignments]

    return ((X-Karanged)**2).sum()