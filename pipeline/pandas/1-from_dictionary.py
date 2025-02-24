#!/usr/bin/env python3
"""Importing pandas for data analysis and manipulation"""
import pandas as pd


dictionary_df = {'First': [0.0, 0.5, 1.0, 1.5],
                 'Second': ['one', 'two', 'three', 'four']}

rows = ['A', 'B', 'C', 'D']

df = pd.DataFrame.from_dict(dictionary_df, orient='columns')

df.index = rows
