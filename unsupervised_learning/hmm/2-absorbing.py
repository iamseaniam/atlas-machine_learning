#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def absorbing(P):
    """Documentation"""
    if not isinstance(P, np.ndarray) or len(
        P.shape) != 2 or P.shape[0] != P.shape[1]:
        return False

    n = P.shape[0]
    absorbing_states = np.array([P[i, i] == 1 for i in range(n)])

    if not np.any(absorbing_states):
        return False

    reachable = np.zeros((n, n), dtype=bool)
    reachable[P > 0] = True

    for k in range(n):
        for i in range(n):
            for j in range(n):
                reachable[i, j] = reachable[
                    i, j] or (reachable[i, k] and reachable[k, j])

    for i in range(n):
        if not absorbing_states[i]:
            if not np.any(reachable[i, absorbing_states]):
                return False

    return True
