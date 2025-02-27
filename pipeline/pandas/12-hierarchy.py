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


def hierarchy(df1, df2):
    """function does A lot, i am sleep"""
    df1.set_index('Timestamp', inplace=True)
    df2.set_index('Timestamp', inplace=True)

    df1_selected = df1.loc[1417411980:1417417980]
    df2_selected = df2.loc[1417411980:1417417980]

    df_hierarchy = pd.concat([df2_selected, df1_selected], keys=[
                             'bitstamp', 'coinbase'])

    df_hierarchy = df_hierarchy.swaplevel(0, 1).sort_index()

    return df_hierarchy
