#!/usr/bin/env python3
"""documentation"""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """Documentation"""
    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride
    
    if padding == 'same':
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding
    
    padded_images = np.pad(images,
                           ((0, 0),
                            (ph, ph),
                            (pw, pw)),
                           mode='constant',
                           constant_values=0)

    output_h = (h + 2 * ph - kh) // sh + 1
    output_w = (w + 2 * pw - kw) // sw + 1
    convolved = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            convolved[:,
                      i,
                      j] = np.sum(padded_images[:,
                                                i*sh:i*sh+kh,
                                                j*sw:j*sw+kw] * kernel, axis=(1, 2))

    return convolved
