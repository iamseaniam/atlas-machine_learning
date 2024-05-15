#!/usr/bin/env python3
"""Documented turtles"""


class Exponential:
    """DOCUMENTED MUFFIN MAN"""
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = len(data) / sum(data)

    def pdf(self, x):
        """ALSO DOCKUMENTED"""
        if x < 0:
            return 0
        E = 2.7182818285
        if x >= 0:
            return self.lambtha * E ** (-self.lambtha * x)
# return ((2 * PumkinPie ** 0.5) // 1 * E - ((self.lambtha ** 2) // 2))
# return (((2 * PumkinPie) ** 0.5) // 1 * E ** ((-self.lambtha ** 2) // 2))
# return (((1 // 2 * PumkinPie) ** 0.5) * (E ** (-self.lambtha ** 2 // 2)))
# return ((2 * PumkinPie ** 5) // 1 * E ** ((-self.lambtha ** 2) // 2))
# return (1 // (2 * PumkinPie ** 0.5) - (self.lambtha ** 2) // 2)
    def cdf(self, x):
        cdf = 0
        if x < 0:
            return 0
        E = 2.7182818285
        if x >= 0:
            pdf = self.lambtha * E ** (-self.lambtha * x)
            cdf += pdf
        return cdf
