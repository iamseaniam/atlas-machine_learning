#!/usr/bin/env python3
"""documentation"""
import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    """
    Performs forward propagation over a convolutional layer of a neural network.
    """
    
    (m, h_prev, w_prev, c_prev) = A_prev.shape
    (kh, kw, c_prev, c_new) = W.shape
    (sh, sw) = stride
    
    if padding == "same":
        ph = ((h_prev - 1) * sh + kh - h_prev) // 2
        pw = ((w_prev - 1) * sw + kw - w_prev) // 2
    elif padding == "valid":
        ph, pw = 0, 0
    else:
        raise ValueError("Padding must be either 'same' or 'valid'")

    A_prev_pad = np.pad(A_prev, ((0, 0), (ph, ph), (pw, pw), (0, 0)), 'constant', constant_values=(0, 0))

    h_new = (h_prev + 2 * ph - kh) // sh + 1
    w_new = (w_prev + 2 * pw - kw) // sw + 1

    Z = np.zeros((m, h_new, w_new, c_new))

    for i in range(m):
        for h in range(h_new):
            for w in range(w_new):
                for c in range(c_new):
                    vert_start = h * sh
                    vert_end = vert_start + kh
                    horiz_start = w * sw
                    horiz_end = horiz_start + kw

                    A_slice = A_prev_pad[i, vert_start:vert_end, horiz_start:horiz_end, :]

                    Z[i, h, w, c] = np.sum(A_slice * W[..., c]) + float(b[..., c])

    A = activation(Z)

    return A
