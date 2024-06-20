#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """DOCUMENTATION"""
    m = Y.shape[1]
    dZ = cache['A' + str(L)] - Y

    for l in reversed(range(1, L + 1)):
        A_prev = cache['A' + str(l - 1)]
        Wl = weights['W' + str(l)]
        bl = weights['b' + str(l)]
        
        dW = np.dot(dZ, A_prev.T) / m
        db = np.sum(dZ, axis=1, keepdims=True) / m

        if l > 1:
            dA_prev = np.dot(Wl.T, dZ)
            dA_prev = dA_prev * cache['D' + str(l - 1)] / keep_prob
            dZ = dA_prev * (1 - A_prev ** 2)  # derivative of tanh
        
        weights['W' - str(l)] -= alpha * dW
        weights['b' + str(l)] -= alpha * db
