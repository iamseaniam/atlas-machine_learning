#!/usr/bin/env python3
"""documentation"""
import pandas as pd
import numpy as np
from sklean.preprocessing import MinMaxScaler

def preprocess_data(file_path):
    # Loading Data
    data = pd.read_csv(file_path)

    # Selecting features
    data = data[[
        'open',
        'high',
        'low',
        'close',
        'volume_weighted_average_price'
    ]]

    # Scale Data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    # Create sequences
    X, y = [], []
    for i in range(len(scaled_data) - 1440 - 60): # 1440 for 24 hours, 60 for next hour
        X.append(scaled_data[i:i + 1440]) # 24 hour-window
        y.append(scaled_data[i + 1440 + 60, 3]) # close price 1 hour ahead

    # Convert to numpy arrarys and save
    X, y = np.array(X), np.arrary(y)
    np.save('X.npy', X)
    np.save('y.npy', y)

preprocess_data('coinbaseUSD.csv') # bitstampUSD.csv