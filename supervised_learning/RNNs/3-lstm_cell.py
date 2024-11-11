#!/usr/bin/env python3
"""documentation"""
import numpy as np


class LSTMCell:
    """_summary_
    """

    def __init__(self, i, h, o):
        """
        Initializes the parameters of the LSTM cell.
        """
        self.Wf = np.random.randn(i + h, h)
        self.bf = np.zeros((1, h))

        self.Wu = np.random.randn(i + h, h)
        self.bu = np.zeros((1, h))

        self.Wc = np.random.randn(i + h, h)
        self.bc = np.zeros((1, h))

        self.Wo = np.random.randn(i + h, h)
        self.bo = np.zeros((1, h))

        self.Wy = np.random.randn(h, o)
        self.by = np.zeros((1, o))

    def forward(self, h_prev, c_prev, x_t):
        """
        Performs forward propagation for one time step in the LSTM cell.
        """
        concat_hx = np.concatenate((h_prev, x_t), axis=1)

        f_t = self.sigmoid(np.dot(concat_hx, self.Wf) + self.bf)

        u_t = self.sigmoid(np.dot(concat_hx, self.Wu) + self.bu)

        c_tilde = np.tanh(np.dot(concat_hx, self.Wc) + self.bc)

        c_next = f_t * c_prev + u_t * c_tilde

        o_t = self.sigmoid(np.dot(concat_hx, self.Wo) + self.bo)

        h_next = o_t * np.tanh(c_next)

        y_linear = np.dot(h_next, self.Wy) + self.by
        y = self.softmax(y_linear)

        return h_next, c_next, y

    def sigmoid(self, x):
        """Helper method for the sigmoid activation function."""
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        """Helper method for the softmax activation function."""
        exps = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exps / np.sum(exps, axis=1, keepdims=True)
