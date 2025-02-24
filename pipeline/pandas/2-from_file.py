#!/usr/bin/env python3
"""Importing pandas for data analysis and manipulation"""
import pandas as pd


def from_file(filename, delimiter):
    """Function loads data from a file as a pandas DataFrame"""
    pd.DataFrame = pd.read_csv(filename, delimiter=delimiter)
    return pd.DataFrame
