#!/bin/usr/env python3
"""ehheeheehheeh documentation """


def summation_i_squared(n):
    """Hmmm this seems dificult"""
    if not isinstance(n, int) or n <= 0:
        return None
    sum = (n * (n + 1) * (2 * n + 1)) // 6
    return sum
