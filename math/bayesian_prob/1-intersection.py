#!/usr/bin/env python3
"""Ducomentation"""


def intersection(x, n, P, Pr):
    """documentation"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError(
            "n must be a positive integer"
            )

    if not isinstance(x, int) or 0 < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )