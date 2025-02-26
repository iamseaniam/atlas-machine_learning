#!/usr/bin/env python3
"""Checker Satisfaction"""


def flip_switch(df):
    """Function sorts data in reverse chrological order.
    Transposes the sorted dataframe.
    Returns: transformed pd.DataFrame."""

    sort_reverse = df.sort_values(by=['Timestamp'], ascending=False)

    tranpose = sort_reverse.transpose()

    return tranpose
