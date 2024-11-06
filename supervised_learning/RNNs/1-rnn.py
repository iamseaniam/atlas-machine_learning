#!/usr/bin/env python3
""" documentation """
import numpy as np


def rnn(rnn_cell, X, h_0):
    """ forward prop for a simple rnn

    Args:
        rnn_cell: is an instance of RNNCell that is used for forward prop
        X (_type_): _description_
        h_0 (_type_): _description_
    """
    # retriving diminsions 
    t, m, i = X.shape
    _, h = h_0.shape

    H = np.zeros((t + 1, m, h))
    Y = np.zeros((t, m, rnn_cell.Wy.shape[1]))

    H[0] = h_0