#!/usr/bin/env python3
"""Checker Satisfaction"""


def analyze(df):
    """function does computive descriptive statistics for all columns"""
    df = df.drop(columns=['Timestamp'])
    df = df.describe(include='all')
    return df
