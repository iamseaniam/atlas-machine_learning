#!/usr/bin/env python3
"""Docmentation"""
import sklearn.cluster as skcls


def kmeans(X, k):
    """Performs K-means on a dataset."""
    centroid, label, inertia = skcls.k_means(X, k)
    return centroid, label
