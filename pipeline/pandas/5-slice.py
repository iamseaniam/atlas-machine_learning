#!/usr/bin/env python3
"""Importing pandas for data analysis and manipulation"""


def slice(df):
    """no idea yet"""

    grab_col = df[["High", "Low", "Close", "Volume_BTC"]]

    grab_row = df[df[grab_col] % 60]

    return grab_row
