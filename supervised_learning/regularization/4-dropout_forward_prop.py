#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """DOCUMENTATION"""
    outputs = {}
    outputs["A0"] = X
    for layer in range(1, L+1):
        w = weights["W{}".format(layer)]
        a = outputs["A{}".format(layer-1)]
        b = weights["b{}".format(layer)]
        z = np.matmul(w, a) + b

        if layer == L:
            t = np.exp(z)
            outputs["A{}".format(layer)] = t/np.sum(t, axis=0)

        else:
            top = np.exp(z) - np.exp(-z)
            bot = np.exp(z) + np.exp(-z)
            a = top / bot

            dx = np.random.rand(a.shape[0], a.shape[1]) < keep_prob
            outputs["D{}".format(layer)] = dx*1
            a *= dx
            a /= keep_prob
            outputs["A{}".format(layer)] = a

    return outputs
