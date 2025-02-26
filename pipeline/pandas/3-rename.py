#!/usr/bin/env python3
"""Importing pandas for data analysis and manipulation"""
import pandas as pd


def rename(df):
    """Renames the Timestamp column to Datetime, converts it to datetime format, 
    and returns only the Datetime and Close columns."""

    # Rename Timestamp to Datetime
    df = df.rename(columns={"Timestamp": "Datetime"})
    # converts timestamp values to datatime values
    df["Datetime"] = pd.to_datetime(df["Datetime"])

    # Returns only required columns
    return df[["Datatime", "Close"]]
