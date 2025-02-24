#!/usr/bin/env python3
"""Importing pandas for data manipulation"""
import pandas as pd


def from_numpy(array):
    """Function that creates a pd.DataFrame from a np.ndarray"""

    column_labels = [chr(65 + i) for i in range(array.shape[1])]

    return pd.DataFrame(array, columns=column_labels)
