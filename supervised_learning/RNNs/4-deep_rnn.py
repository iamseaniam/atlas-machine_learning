#!/usr/bin/env python3
"""documentation"""
import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """_summary_

    Args:
        rnn_cells (_type_): _description_
        X (_type_): _description_
        h_0 (_type_): _description_
    """
    t, m, i = X.shape
    l, _, h = h_0.shape

    H = np.zeros((t + 1, l, m, h))
    Y = []

    H[0] = h_0

    for time_step in range(t):
        x_t = X[time_step]

        for layer in range(l):
            rnn_cell = rnn_cells[layer]

            h_prev = H[time_step, layer]
            h_next, y = rnn_cell.forward(h_prev, x_t)

            H[time_step + 1, layer] = h_next

            x_t = h_next

        Y.append(y)

    Y = np.stack(Y, axis=0)

    return H, Y
