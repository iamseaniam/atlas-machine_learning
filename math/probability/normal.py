#!/usr/bin/env python3
"""sadness baanan brains"""


class Normal:
    """ This is a class, damn thats cool """
    def __init__(self, data=None, mean=0., stddev=1.):
        """ MUAHHAUAHUAHUAHUHAUHHUA """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data)) / len(data)
            self.stddev = (
                (sum((x - self.mean) ** 2 for x in data)
                    / len(data)) ** 0.5
                )
            if self.stddev <= 0:
                raise ValueError("stddev must be a positive value")

    def z_score(self, x):
        """Movies, picnic"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Cowboys
        """
        return z * self.stddev + self.mean

    def pdf(self, x):
        """values are crazy"""
        π = 3.1415926536
        e = 2.7182818285
        coefficient = 1 / (self.stddev * (2 * π) ** 0.5)
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        return coefficient * e ** exponent 
