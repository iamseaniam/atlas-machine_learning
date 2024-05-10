#!/usr/bin/env python3
"""HELLO WORLD ITS BOB"""

def poly_integral(poly, C=0):
    """I am not bob, im sorry for lying """
    if not isinstance(poly, list) or not all(isinstance(x, (int, float)) for x in poly) or not isinstance(C, int):
        return None

    if len(poly) == 0:
        return None

    integral_poly = [0] * (len(poly) + 1)
    for i in range(1, len(integral_poly)):
        integral_poly[i] = poly[i - 1] / i

    integral_poly[0] = C

    while integral_poly[-1] == 0 and len(integral_poly) > 1:
        integral_poly.pop()

    return integral_poly
