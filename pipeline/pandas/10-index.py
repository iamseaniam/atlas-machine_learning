#!/usr/bin/env python3
"""Checker Satisfaction"""


def index(df):
    """Function sets Timestamp as the index of the dataframe"""
    index = df.set_index('Timestamp')

    return index
