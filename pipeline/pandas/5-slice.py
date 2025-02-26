#!/usr/bin/env python3
"""Checker Satisfaction"""


def slice(df):
    """Function grabs columns, every 60th row for columns.
    returns new sliced pd.DataFrame"""

    grab_col = df[["High", "Low", "Close", "Volume_(BTC)"]]

    grab_row = grab_col.iloc[::60, :]

    return grab_row
