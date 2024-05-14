#!/usr/bin/env python3
"""This documented throughly"""


class Poisson:
    """Mushrooms make some weird noises"""
    def __init__(self, data=None, lambtha=1.):
        """This class represents a Poisson distribution."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")


    def pmf(self, k):
        """Bull lone e"""
        k = int(k)
        if k < 0:
            return 0
        else:
            e = 2.7182818285
            factorial_k = 1
            for i in range(1, k + 1):
                factorial_k *= i
            return (e ** -self.lambtha * (self.lambtha ** k)) / factorial_k


    def cdf(self, k):
        k = int(k)
        if k < 0:
            return 0
        else:
            e = 2.7182818285
            cumulative_probability = 0
            factorial_i = 1
            for i in range(0, k + 1):
                calc = (e ** -self.lambtha * (self.lambtha ** factorial_i)) / factorial_i
                cumulative_probability += calc
                factorial_i += (i + 1)
            return cumulative_probability
