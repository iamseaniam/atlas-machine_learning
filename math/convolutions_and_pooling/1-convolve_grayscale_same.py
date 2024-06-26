#!/usr/bin/env python3
"""documentation"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """Documentation"""
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph = kh // 2
    pw = kw // 2

    padded_images = np.pad(images,
                           ((0, 0),
                            (ph, ph),
                            (pw, pw)),
                           mode='constant',
                           constant_values=0)

    convolved = np.zeros((m, h, w))

    for i in range(h):
        for j in range(w):
            convolved[:,
                      i,
                      j] = np.sum(padded_images[:,
                                                i:i+kh,
                                                j:j+kw] * kernel, axis=(1, 2))

    return convolved
