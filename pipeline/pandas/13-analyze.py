#!/usr/bin/env python3
"""Checker Satisfaction"""


def analyze(df):
    """function does computive descriptive statistics for all columns"""
    stats = df[['Open', 'High', 'Low', 'Close',
               'Volume_(BTC)', 'Weighted_Price']].describe()
    return stats
