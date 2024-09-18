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
    # Compute the Covariance Matrix
    #   np.cov(), use rowvar=False
    np.cov(X, rowvar=False)
    # Perform Eigen Decomposition
    #   np.linalg.eigh()
    eigva, eigve = np.linalg.eigh(X)
    # Sort Eigenvalues and Eigenvectors
    #   np.argsort()
    np.argsort(eigva, eigve)
    # Determine the Number of Principal Compoents
    #   np.cumsum(), or np.sum()
    
    # Select the top Eigenvectors
    #   indexing
    
    # Return the Weights Matrix

