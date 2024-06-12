#!/usr/bin/env python3
"""DOCUMENTATION"""
import numpy as np


def normalization_constants(X):
    """DOCUMENTATION"""
    m = np.sum(X, axis=0) / X.shape[0]
    s = np.sqrt(np.sum((X - m)**2, axis=0) / X.shape[0])
    return (m, s)
