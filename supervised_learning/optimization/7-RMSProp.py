#!/usr/bin/env python3
"""DOCUMENTATION"""
import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """DOCUMENTATION"""
    sdw = (beta2*s) + ((1-beta2)*(grad**2))
    return var - (alpha * (grad/((sdw ** (1/2)) + epsilon))), sdw
