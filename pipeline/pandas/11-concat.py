#!/usr/bin/env python3
"""Checker Satisfaction"""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """no idea yet"""
    df1.set_index('Timestamp', inplace=True)
    df2.set_index('Timestamp', inplace=True)

    df2_selected = df2.loc[:1417411920]

    df_conCAT = pd.concat([df2_selected, df1], keys=['bitstamp', 'coinbase'])

    return df_conCAT
