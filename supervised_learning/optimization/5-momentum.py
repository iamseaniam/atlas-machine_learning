#!/usr/bin/env python3
"""DOCUMENTATION"""
import numpy as np


def update_variables_momentum(alpha, beta1, var, grad, v):
    """DOCUMENTATION"""
    new = (v*beta1) + (grad*(1-beta1))
    return var - (new*alpha), new
