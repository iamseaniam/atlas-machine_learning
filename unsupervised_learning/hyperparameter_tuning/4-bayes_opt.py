#!/usr/bin/env python3
"""
Creates class that performs Bayesian optimization
on a noiseless 1D Gaussian process
"""


from scipy.stats import norm
import numpy as np
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization:
    """
    Performs Bayesian optimization on a noiseless 1D Gaussian process
    """
    def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1,
                 sigma_f=1, xsi=0.01, minimize=True):
        """
        Class constructor
        """
        if type(X_init) is not np.ndarray or len(X_init.shape) != 2:
            raise TypeError("X_init must be numpy.ndarray of shape (t, 1)")
        t, one = X_init.shape
        if one != 1:
            raise TypeError("X_init must be numpy.ndarray of shape (t, 1)")
        if type(Y_init) is not np.ndarray or len(Y_init.shape) != 2:
            raise TypeError("Y_init must be numpy.ndarray of shape (t, 1)")
        t_check, one = Y_init.shape
        if one != 1 or t_check != t:
            raise TypeError("Y_init must be numpy.ndarray of shape (t, 1)")
        if type(bounds) is not tuple or len(bounds) != 2:
            raise TypeError("bounds must be a tuple of (min, max)")
        min, max = bounds
        if type(min) is not int and type(min) is not float:
            raise TypeError("min in bounds must be int or float")
        if type(max) is not int and type(max) is not float:
            raise TypeError("max in bounds must be int or float")
        if min >= max:
            raise ValueError("min from bounds must be less than max")
        if type(l) is not int and type(l) is not float:
            raise TypeError(
                "l must be int or float to represent kernel length parameter")
        if type(sigma_f) is not int and type(sigma_f) is not float:
            raise TypeError(
                "sigma_f must be int or float to represent standard deviation")
        if type(xsi) is not int and type(xsi) is not float:
            raise TypeError(
                "xsi must be int or float to represent \
                exploration-exploitation factor")
        if type(minimize) is not bool:
            raise TypeError("minimize must be boolean to indicate if \
            optimization should be formed for minimization or maximization")
        self.f = f
        self.gp = GP(X_init, Y_init, l, sigma_f)
        self.X_s = X_init
        self.xsi = xsi
        self.minimize = minimize

    def acquisition(self):
        """
        docujaenm
        """
        return None, None