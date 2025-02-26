#!/usr/bin/env python3
"""Importing pandas for data analysis and manipulation"""
import pandas as pd


def rename(df):
    """no idea yet"""

    df = pd.DataFrame

    # Renaming timestamp column to Datetime
    # inplace modifies original pd.DataFrame when set to "True"
    renamed_column = df.rename(columns={'Timestamp': 'Datetime'}, inplace=True)

    pd.to_datetime(renamed_column)
    df[['Datetime', 'Close']]
