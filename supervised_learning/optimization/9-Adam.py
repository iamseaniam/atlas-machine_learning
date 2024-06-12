#!/usr/bin/env python3
"""DOCUMENTATION"""
import numpy as np


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """DOCUMENTATION"""
    Vdw, Sdw = 0, 0
    Vdw = (beta1*v) + ((1 - beta1)*grad)
    Vdw_bias_correct = Vdw/(1 - (beta1 ** t))
    Sdw = (beta2*s) + ((1 - beta2)*(grad**2))
    Sdw_bias_correct = Sdw/(1 - (beta2 ** t))
    adam = (Vdw_bias_correct)/((Sdw_bias_correct ** (1/2))+epsilon)
    return var - alpha * adam, Vdw, Sdw
