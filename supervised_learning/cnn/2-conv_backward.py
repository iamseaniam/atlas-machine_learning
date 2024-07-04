#!/usr/bin/env python3
"""documentation"""
import numpy as np


def conv_backward(dZ, A_prev, W, b, padding="same", stride=(1, 1)):
    """
    Performs back propagation over a convolutional layer of a neural network.
    """

    (m, h_prev, w_prev, c_prev) = A_prev.shape
    (kh, kw, c_prev, c_new) = W.shape
    (sh, sw) = stride
    (m, h_new, w_new, c_new) = dZ.shape

    if padding == "same":
        ph = ((h_prev - 1) * sh + kh - h_prev) // 2
        pw = ((w_prev - 1) * sw + kw - w_prev) // 2
    elif padding == "valid":
        ph, pw = 0, 0
    else:
        raise ValueError("Padding must be either 'same' or 'valid'")

    A_prev_pad = np.pad(A_prev, ((0, 0), (ph, ph), (pw, pw), (0, 0)), 'constant', constant_values=(0, 0))
    dA_prev_pad = np.pad(np.zeros_like(A_prev), ((0, 0), (ph, ph), (pw, pw), (0, 0)), 'constant', constant_values=(0, 0))

    dW = np.zeros_like(W)
    db = np.zeros_like(b)

    for i in range(m):
        a_prev_pad = A_prev_pad[i]
        da_prev_pad = dA_prev_pad[i]

        for h in range(h_new):
            for w in range(w_new):
                for c in range(c_new):
                    vert_start = h * sh
                    vert_end = vert_start + kh
                    horiz_start = w * sw
                    horiz_end = horiz_start + kw
                    
                    a_slice = a_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :]
                    
                    da_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :] += W[..., c] * dZ[i, h, w, c]
                    dW[..., c] += a_slice * dZ[i, h, w, c]
                    db[..., c] += dZ[i, h, w, c]
        dA_prev_pad[i] = da_prev_pad

    if padding == "same":
        dA_prev = dA_prev_pad[:, ph:-ph, pw:-pw, :]
    elif padding == "valid":
        dA_prev = dA_prev_pad

    return dA_prev, dW, db

