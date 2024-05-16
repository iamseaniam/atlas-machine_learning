#!/usr/bin/env python 3
"""DOCUMENTATION"""

class Binomial:
    """DOCUMERNTST"""
    def __init__(self, data=None, n=1, p=0.5):
        """DOCUMENTATION"""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not 0 < p < 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            num_successes = sum(1 for outcome in data if outcome)
            p = num_successes / len(data)
            n = len(data) / p
            n = round(n)
            p = num_successes / n
            self.n = n
            self.p = p

    def pmf(self, k):
        """DIKJFHUSIHFIJFIJFIFS"""
        k = int(k)
        if not 0 <= k <= self.n: 
            return 0
        binomial_coefficient = self._binomial_coefficient(self.n, k)
        probability_of_success = self.p ** k
        probability_of_failure = (1 - self.p) ** (self.n - k)
        return binomial_coefficient * probability_of_success * probability_of_failure
