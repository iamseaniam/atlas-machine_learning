#!/usr/bin/env python3
"""Checker Satisfaction"""


def prune(df):
    """Removes any entries where "Close" has NaN values"""
    remove_NaN = df.dropna(subset=['Close'])

    return remove_NaN
