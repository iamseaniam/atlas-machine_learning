#!/usr/bin/env python3
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import LSTM, Dense # type: ignore

def load_data():
    X = np.load('X.npy')
    y = np.load
    dataset = tf.data.Dataset.from_tensor_slices((X, y))
    dataset = dataset.shuffle(buffer_size=10000).batch(64) # <- Can Ajust batch size
    return dataset

def create_model():
    model = Sequential([
        LSTM(128, return_sequences=True, input_shape=(1440, 5)),
        LSTM(64),
        Dense(32, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_model():
    dataset = load_data()
    model = create_model()

    # Split into traininf and validation
    train_size = int(0.8 * len(dataset))
    train_dataset = dataset.take(train_size)
    val_dataset = dataset.skip(train_size)

    model.fit(train_dataset, epochs=10, validation_data=val_dataset)
    model.save('btc_forecast_model.h5')

train_model()