#!/usr/bin/env python3
"""Docmentation"""
import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """Performs the expectation step in the EM algorithm for a GMM."""
    if (type(X) is not np.ndarray or X.ndim != 2 or
        type(pi) is not np.ndarray or pi.ndim != 1 or
        type(m) is not np.ndarray or m.ndim != 2 or
        type(S) is not np.ndarray or S.ndim != 3):
        return None, None

    n, d = X.shape
    k = pi.shape[0]

    if (m.shape != (k, d) or S.shape != (k, d, d) or 
        not np.isclose(np.sum(pi), 1)):
        return None, None

    g = np.zeros((k, n))

    for i in range(k):
        P = pdf(X, m[i], S[i])
        if P is None:
            return None, None
        g[i] = pi[i] * P

    total_prob = np.sum(g, axis=0)

    log_likelihood = np.sum(np.log(total_prob))

    g /= total_prob

    return g, log_likelihood
