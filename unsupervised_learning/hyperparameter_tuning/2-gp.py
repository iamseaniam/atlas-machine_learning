#!/usr/bin/env python3
"""Python documentation"""
import numpy as np


class GaussianProcess:
    """Documentation"""
import numpy as np

class GaussianProcess:
    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        """
        Class constructor for a 1D Gaussian Process
        """
        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(self.X, self.X)

    def kernel(self, X1, X2):
        """
        Computes the covariance kernel matrix using the RBF kernel
        """
        sqdist = np.sum(X1**2, 1).reshape(-1, 1) + np.sum(
            X2**2, 1) - 2 * np.dot(X1, X2.T)

        return self.sigma_f**2 * np.exp(-0.5 / self.l**2 * sqdist)
    
    def predict(self, X_s):
        """
        Predicts the mean and standard deviation of points in a Gaussian process
        """
        K_s = self.kernel(X_s, self.X)
        K_ss = self.kernel(X_s, X_s)
        K_inv = np.linalg.inv(self.K)
        mu_s = K_s.dot(K_inv).dot(self.Y).flatten()
        sigma_s = K_ss - K_s.dot(K_inv).dot(K_s.T)
        sigma_s = np.diag(sigma_s)
        return mu_s, sigma_s

    def update(self, X_new, Y_new):
        """
        Updates the Gaussian Process with a new sample point
        """
        self.X = np.vstack([self.X, X_new.reshape(-1, 1)])
        self.Y = np.vstack([self.Y, Y_new.reshape(-1, 1)])
        self.K = self.kernel(self.X, self.X)
