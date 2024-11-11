#!/usr/bin/env python3
"""documentation"""
import numpy as np


class GRUCell:
    """documentation"""

    def __init__(self, i, h, o):
        """
        Initialize the parameters of the GRU cell.
        """
        self.Wz = np.random.randn(i + h, h)
        self.bz = np.zeros((1, h))

        self.Wr = np.random.randn(i + h, h)
        self.br = np.zeros((1, h))

        self.Wh = np.random.randn(i + h, h)
        self.bh = np.zeros((1, h))

        self.Wy = np.random.randn(h, o)
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        Perform forward propagation for one time step.
        """
        concat_hx = np.concatenate((h_prev, x_t), axis=1)

        z_t = self.sigmoid(np.dot(concat_hx, self.Wz) + self.bz)

        r_t = self.sigmoid(np.dot(concat_hx, self.Wr) + self.br)

        concat_reset_hx = np.concatenate((r_t * h_prev, x_t), axis=1)
        h_tilde = np.tanh(np.dot(concat_reset_hx, self.Wh) + self.bh)

        h_next = (1 - z_t) * h_prev + z_t * h_tilde

        y_linear = np.dot(h_next, self.Wy) + self.by
        y = self.softmax(y_linear)

        return h_next, y

    def sigmoid(self, x):
        """Helper method for the sigmoid activation function."""
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        """Helper method for the softmax activation function."""
        exps = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exps / np.sum(exps, axis=1, keepdims=True)
