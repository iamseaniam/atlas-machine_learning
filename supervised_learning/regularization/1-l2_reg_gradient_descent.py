#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """DOCUMENTATION"""
    m = Y.shape[1]
    A_prev = cache['A' + str(L)]
    dA = A_prev - Y 

    for i in reversed(range(1, L + 1)):
        A_prev = cache['A' + str(i - 1)] if i > 1 else cache['A0']
        W = weights['W' + str(i)]
        b = weights['b' + str(i)]
        
        dZ = dA
        dW = (1 / m) * np.dot(dZ, A_prev.T) + (lambtha / m) * W
        db = (1 / m) * np.sum(dZ, axis=1, keepdims=True)
        
        weights['W' + str(i)] = W - alpha * dW
        weights['b' + str(i)] = b - alpha * db

        if i > 1:
            dA = np.dot(W.T, dZ) * (1 - np.square(A_prev))
