#!/usr/bin/env python3
"""Checker Satisfaction"""


def fill(df):
    """This function removes the "Weighted_price" column
    fills missing values in "Clo se" column
    fills missing values for "High", "Low", "Open"
    Sets missing values "Volume_BTC", and "Volumn_Currency to 0"""

    df = df.drop(columns=['Weighted_Price'])

    df['Close'].fillna(method='ffill', inplace=True)

    for col in ['High', 'Low', 'Open']:
        df[col].fillna(df['Close'], inplace=True)

    df[["Volume_(BTC)", "Volume_(Currency)"]] = df[[
        "Volume_(BTC)", "Volume_(Currency)"]].fillna(0)

    return df
