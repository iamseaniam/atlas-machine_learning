#!/usr/bin/env python3
"""modulefunction"""
import numpy as np


def one_hot_decode(one_hot):
    """normal vector"""
    if type(one_hot) is not np.ndarray:
        return None
    if one_hot.ndim != 2:
        return None
    return one_hot.T.nonzero()[1]
