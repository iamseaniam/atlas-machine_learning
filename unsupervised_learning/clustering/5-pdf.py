#!/usr/bin/env python3
"""Docmentation"""
import numpy as np


def pdf(X, m, S):
    """Calculates the PDF of a Gaussian distribution."""
    if not isinstance(X, 
                      np.ndarray) or not isinstance(
                          m, np.ndarray) or not isinstance(S, np.ndarray):
        return None

    d = X.shape[1]

    det_S = np.linalg.det(S)
    inv_S = np.linalg.inv(S)

    norm_factor = 1 / np.sqrt((2 * np.pi) ** d * det_S)

    diff = X - m
    exponent = -0.5 * np.sum(diff @ inv_S * diff, axis=1)

    P = norm_factor * np.exp(exponent)
    
    return np.maximum(P, 1e-300)
