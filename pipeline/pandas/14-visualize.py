#!/usr/bin/env python3
"""Import mtplotlib to plot data
Importing pandas for data mulniulation and alyaises"""
import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Drop the column Weighted_Price
df = df.drop(columns=['Weighted_Price'])

# Rename the column Timestamp to Date
df = df.rename(columns={'Timestamp': 'Date'})

# Convert the timestamp values to date values
df['Date'] = pd.to_datetime(df['Date'], unit='s')

# Set Date as index
df.set_index('Date', inplace=True)

# Missing values in Close should be set to the previous row value
df['Close'].fillna(method='ffill', inplace=True)

# Missing values in High, Low, Open should be set to the same rows Close value
df[['High', 'Low', 'Open']] = df[[
    'High', 'Low', 'Open']].fillna(df['Close'], axis=0)

# Missing values in Volume_(BTC) and Volume_(Currency) should be set to 0
df[['Volume_(BTC)', 'Volume_(Currency)']] = df[[
    'Volume_(BTC)', 'Volume_(Currency)']].fillna(0)

# Filter data from 2017 to current
df = df[df.index >= '2017-01-01']

df_daily = df.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

# Return transformed DataFrame before plotting
print(df_daily)

# Plot Close price over time
plt.figure(figsize=(12, 6))
plt.plot(df_daily.index, df_daily['High'], label='Close Price', color='blue')
plt.plot(df_daily.index, df_daily['Low'], label='Close Price', color='yellow')
plt.plot(df_daily.index, df_daily['Open'], label='Close Price', color='green')
plt.plot(df_daily.index, df_daily['Close'], label='Close Price', color='red')
plt.plot(df_daily.index, df_daily['Volume_(BTC)'],
         label='Close Price', color='violet')
plt.plot(df_daily.index,
         df_daily['Volume_(Currency)'], label='Close Price', color='brown')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.title('Bitcoin Daily Close Price (2017 and Beyond)')
plt.legend()
plt.grid()
plt.show()
