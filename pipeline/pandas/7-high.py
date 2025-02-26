#!/usr/bin/env python3
"""Checker Satisfaction"""


def high(df):
    """function sorts the column "High" data in descending order"""
    sort_desc = df.sort_values(by=['High'], ascending=False)

    return sort_desc
