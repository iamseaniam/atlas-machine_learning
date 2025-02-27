#!/usr/bin/env python3
"""Checker Satisfaction"""


def fill(df):
    """This function removes the "Weighted_price" column
    fills missing values in "Clo se" column
    fills missing values for "High", "Low", "Open"
    Sets missing values "Volume_BTC", and "Volumn_Currency to 0"""

    filled_df = df.drop('Weighted_Price', axis=1)

    filled_df.loc[:, ["Close"]] = filled_df.loc[: ["Close"]].ffill()

    filled_df.loc["High"] = filled_df["High"].fillna(filled_df["Close"])

    filled_df.loc["Low"] = filled_df["Low"].fillna(filled_df["Close"])

    filled_df.loc["Open"] = filled_df["Open"].fillna(filled_df["Close"])

    filled_df[["Volume_(BTC)", "Volume_(Currency)"]] = filled_df[[
        "Volume_(BTC)", "Volume_(Currency)"]].fillna(value=0)

    return filled_df
