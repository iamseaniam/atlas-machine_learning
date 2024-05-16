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
        coefficient = 1 / (self.stddev * (2 * 3.14159) ** 0.5)
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        return coefficient * 2.71828 ** exponent

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value"""
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))
        erf_value = self._erf(z)
        return 0.5 * (1 + erf_value)
