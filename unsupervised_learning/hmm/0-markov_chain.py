#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def markov_chain(P, s, t=1):
    """Documentation"""
    if not isinstance(P, np.ndarray) or not isinstance(s, np.ndarray):
        return None
    if P.shape[0] != P.shape[1]:
        return None
    if s.shape != (1, P.shape[0]):
        return None

    for _ in range(t):
        s = np.dot(s, P)

    return s
