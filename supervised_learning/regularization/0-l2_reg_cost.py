#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """DOCUMENTATION"""
    l2_costatron = cost
    l2_termialCancer = 0

    for i in range(1, L + 1):
        weight_key = 'W' + str(i)
        l2_termialCancer += np.sum(np.square(weights[weight_key]))
    l2_costatron += (lambtha / (2 * m)) * l2_termialCancer

    return l2_costatron
