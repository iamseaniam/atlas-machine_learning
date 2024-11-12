#!/usr/bin/env python3
"""documentation"""
import numpy as np


class BidirectionalCell:
    """documentation"""

    def __init__(self, i, h, o):
        """_summary_"""
        self.Whf = np.random.randn(i + h, h)
        self.bhf = np.zeros((1, h))

        self.Whb = np.random.randn(i + h, h)
        self.bhb = np.zeros((1, h))

        self.Wy = np.random.randn(2 * h, o)
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        Calculates the forward hidden state for one time step.
        """
        concat_input = np.concatenate((h_prev, x_t), axis=1)

        h_next = np.tanh(np.matmul(concat_input, self.Whf) + self.bhf)

        return h_next

    def backward(self, h_next, x_t):
        """
        to long
        """
        concat_input = np.concatenate((h_next, x_t), axis=1)

        h_pev = np.tanh(np.dot(concat_input, self.Whb) + self.bhb)

        return h_pev
