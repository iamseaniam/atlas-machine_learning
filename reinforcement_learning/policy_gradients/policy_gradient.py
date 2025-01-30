#!/usr/bin/env python3
"""documentation"""
import numpy as np


def policy(matrix, weight):
    """Compute the policy with a weight of a matrix."""
    z = matrix.dot(weight)
    exp = np.exp(z - np.max(z))
    return exp / np.sum(exp)


def policy_gradient(state, weight):
    """
    Compute the Monte-Carlo policy gradient
    based on a state and a weight matrix.
    """
    probs = policy(state, weight)
    action = np.random.choice(len(probs), p=probs)
    d_softmax = probs.copy()
    d_softmax[action] -= 1
    gradient = -np.outer(state, d_softmax)
    return action, gradient
