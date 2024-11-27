#!/usr/bin/env python3
"""documentation"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(file_path):
    # Loading Data
    data = pd.read_csv(file_path)

    # Selecting features
    data = data[[
        'Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price'
        # 'Open',
        # 'High',
        # 'Low',
        # 'Close',
        # 'Weighted_Price'
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

preprocess_data('/home/sean/ml/tf_gpu/atlas-machine_learning/supervised_learning/time_series/coinbaseUSD.csv') # bitstampUSD.csv