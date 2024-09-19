#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def pca(X, var=0.95):
    """
    X = np.ndarray shape of (n, d)
        n = num of data points
        d = num of dimensions in each point
    var = fraction of the variance that PCA tranformation should matain
    """
    u, sig, v = np.linalg.svd(X)
    sum = np.sum(sig)
    trunc = X.shape[1]
    cmsm = np.cumsum(sig)/sum
    trunc = np.where(cmsm >= var)[0][0] + 1
    return v.T[:, :trunc]
