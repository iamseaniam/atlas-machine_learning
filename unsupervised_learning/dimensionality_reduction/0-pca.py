#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def pca(X, var=0.95):
    """Documentation"""
    cov_matrix = np.cov(X, rowvar=False)

    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    sorted_idx = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_idx]
    sorted_eigenvectors = eigenvectors[:, sorted_idx]

    cum_var_explained = np.cumsum(sorted_eigenvalues) / np.sum(sorted_eigenvalues)

    num_components = np.searchsorted(cum_var_explained, var) + 1

    W = sorted_eigenvectors[:, :num_components]

    return W

