#!/usr/bin/env python3
"""DOCUMENTATION"""
import numpy as np


def batch_norm(Z, gamma, beta, epsilon):
    """DOCUMENTATION"""
    mean = np.mean(Z, axis=0)
    var = np.var(Z, axis=0)
    z_norm = (Z - mean) / ((var + epsilon) ** (1/2))
    z_norm_param = (z_norm * gamma) + beta
    return z_norm_param
