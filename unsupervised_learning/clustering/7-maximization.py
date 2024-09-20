#!/usr/bin/env python3
"""Docmentation"""
import numpy as np


def maximization(X, g):
    """Performs the maximization step in the EM algorithm for a GMM."""
    if type(X) is not np.ndarray or X.ndim != 2:
        return None, None, None
    if type(g) is not np.ndarray or g.ndim != 2:
        return None, None, None

    n, d = X.shape
    k, n_g = g.shape

    if n != n_g:
        return None, None, None

    Nk = np.sum(g, axis=1)

    pi = Nk / n
    
    m = np.dot(g, X) / Nk[:, np.newaxis]

    S = np.zeros((k, d, d))
    
    for i in range(k):
        X_mu = X - m[i]
        gamma = g[i][:, np.newaxis]
        S[i] = np.dot(gamma * X_mu.T, X_mu) / Nk[i]

    return pi, m, S
