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
