#!/usr/bin/env python3
"""Python documentation"""
import numpy as np
from scipy.stats import norm
GP = __import__('2-gp').GaussianProcess


np.set_printoptions(precision=8)
class BayesianOptimization:
    """Documentation"""
    def __init__(self, f, X_init, Y_init,
                 bounds, ac_samples, l=1, sigma_f=1,
                 xsi=0.01, minimize=True):
        """
        Class constructor for Bayesian Optimization on a noiseless 1D Gaussian
        """
        self.f = f
        self.gp = GP(X_init, Y_init, l=l, sigma_f=sigma_f)
        self.X_s = np.linspace(bounds[0], bounds[1], ac_samples).reshape(-1, 1)
        self.xsi = xsi
        self.minimize = minimize

    def acquisition(self):
        """
        Calculates the next best sample location using Expected Improvement (EI)
        """
        mu_s, sigma_s = self.gp.predict(self.X_s)
        mu_opt = np.min(self.gp.Y) if self.minimize else np.max(self.gp.Y)

        if self.minimize:
            improvement = mu_opt - mu_s - self.xsi
        else:
            improvement = mu_s - mu_opt - self.xsi

        with np.errstate(divide='warn'):
            Z = improvement / sigma_s
            ei = improvement * norm.cdf(Z) + sigma_s * norm.pdf(Z)
            ei[sigma_s == 0.0] = 0.0

        X_next = self.X_s[np.argmax(ei)]

        return X_next, ei
