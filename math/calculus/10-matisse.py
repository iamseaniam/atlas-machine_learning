#!/usr/bin/env python3
"""Documenttation"""


def poly_derivative(poly):
    """DOCumentation"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    derivative = [i * coeff for i, coeff in enumerate(poly)]
    derivative = [coeff - 1 for coeff in derivative]
    if derivative == [0]:
        return [0]

    return derivative
