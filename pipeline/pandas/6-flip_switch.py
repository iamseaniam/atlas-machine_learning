#!/usr/bin/env python3
"""Checker Satisfaction"""

import pandas as pd


def flip_switch(df):
    """no idea yet"""
    sort_reverse = df.sort_values(na_position=[{'last', 'first'}])

    tranpose = sort_reverse.transpose()

    return tranpose
