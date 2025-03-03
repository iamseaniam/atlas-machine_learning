#!/usr/bin/env python3
"""Ducomentation"""
import numpy as np


def likelihood(x, n, P):
    """documentation"""
    WoahN = 1
    WoahX = 1
    WoahNX = 1
    # Woah means factorial of that var
    # n! / x!(n - x)!

    if not isinstance(n, int) or n <= 0:
        raise ValueError(
            "n must be a positive integer"
            )

    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
            )

    if x > n:
        raise ValueError(
            "x cannot be greater than n"
            )

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError(
            "P must be a 1D numpy.ndarray"
            )

    if not np.all((0 <= P) & (P <= 1)):
        raise ValueError(
            "All values in P must be in the range [0, 1]"
            )

    for i in range(1, n + 1):
        WoahN *= i

    for i in range(1, x + 1):
        WoahX *= i

    for i in range(1, (n - x) + 1):
        WoahNX *= i

    binoial_coeff = WoahN // (WoahX * WoahNX)

    likelihoods = binoial_coeff * (P ** x) * ((1 - P) ** (n - x))

    return likelihoods


def intersection(x, n, P, Pr):
    """"Documentation"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError(
            "n must be a positive integer"
            )

    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
            )

    if x > n:
        raise ValueError(
            "x cannot be greater than n"
            )

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError(
            "P must be a 1D numpy.ndarray"
            )

    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError(
            "Pr must be a numpy.ndarray with the same shape as P"
            )

    # Check if all values in P and Pr are between 0 and 1
    if not np.all((0 <= P) & (P <= 1)):
        raise ValueError(
            "All values in P must be in the range [0, 1]"
            )

    if not np.all((0 <= Pr) & (Pr <= 1)):
        raise ValueError(
            "All values in Pr must be in the range [0, 1]"
            )

    # Check if Pr sums to 1
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError(
            "Pr must sum to 1"
            )

    likelihoods = likelihood(x, n, P)

    intersection_values = likelihoods * Pr

    return intersection_values
