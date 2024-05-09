#!/usr/bin/env python3
"""Documenttation"""


def poly_derivative(poly):
    """Hello world turtles"""
    if not isinstance(poly, list) or not all(isinstance(coef, (int, float)) for coef in poly):
        return None
    n = len(poly)
    if n == 0:
        return None
    derivative = [coef * i for i, coef in enumerate(poly)][1:]
    if all(coef == 0 for coef in derivative):
        return [0]

    return derivative
