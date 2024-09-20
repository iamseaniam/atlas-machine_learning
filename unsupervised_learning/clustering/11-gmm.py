#!/usr/bin/env python3
"""Docmentation"""
import numpy as np
import sklearn.cluster


def gmm(X, k):
    """Calculates a GMM from a dataset using k clusters."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None, None, None
    if not isinstance(k, int) or k <= 0:
        return None, None, None, None, None

    gmm_model = sklearn.cluster.GaussianMixture(n_components=k)
    gmm_model.fit(X)

    pi = gmm_model.weights_
    m = gmm_model.means_
    S = gmm_model.covariances_
    clss = gmm_model.predict(X)
    bic = gmm_model.bic(X)
    
    return pi, m, S, clss, bic
