#!/usr/bin/env python3
"""Documentation"""
import numpy as np


class RNNCell:
    """ Represents a cell of a simple RNN """

    def __init__(self, i, h, o):
        """ class constructor

        Args:
            i: int, dimensionality of the data
            h: int, dimensionality of the hidden state
            o: int, dimensionality of the outputs
        """
        # !: uses randn instead or normal bc its shorthand/ easier
        self.Wh = np.random.randn(h + i, h)
        # !: wraps it again to give it tuple
        self.bh = np.zeros((1, h))

        self.Wy = np.random.randn(h, o)
        self.by = np.zeros((1, o))

    def softmax(self, z):
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def forward(self, h_prev, x_t):
        """ performs forward prop for one time step
        Args:
            h_prev numpy.ndarray:
                contains previous hidden state, shape (m, h)
            x_t numpy.ndarray:
                contains input data for the cell, shape (m, i)
        """
        concatenated = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.dot(concatenated, self.Wh) + self.bh)

        y_raw = np.dot(h_next, self.Wy) + self.by
        y = self.softmax(y_raw)

        return h_next, y