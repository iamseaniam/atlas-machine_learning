#!/usr/bin/env python3
"""Docmentation"""
import sklearn.mixture


def gmm(X, k):
    """Calculates a GMM from a dataset using k clusters."""
    gm = sklearn.mixture.GaussianMixture(k).fit(X)
    return gm.weights_, gm.means_, gm.covariances_, gm.predict(X), gm.bic(X)
