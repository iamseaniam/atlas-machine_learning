#!/usr/bin/env python3
"""Documentation"""
import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """Documentation"""
    inputs = keras.layers.Input(shape=(input_dims,))
    x = inputs
    for nodes in hidden_layers:
        x = keras.layers.Dense(nodes, activation='relu')(x)

    mean = keras.layers.Dense(latent_dims, activation=None)(x)
    log_variance = keras.layers.Dense(latent_dims, activation=None)(x)

    def sampling(args):
        mean, log_variance = args
        epsilon = keras.backend.random_normal(shape=tf.shape(mean))
        return mean + keras.backend.exp(0.5 * log_variance) * epsilon

    latent_space = keras.layers.Lambda(sampling)([mean, log_variance])

    encoder = keras.models.Model(
        inputs,[latent_space, mean, log_variance], name='encoder')

    latent_inputs = keras.layers.Input(shape=(latent_dims,))
    x = latent_inputs

    for nodes in reversed(hidden_layers):
        x = keras.layers.Dense(nodes, activation='relu')(x)

    outputs = keras.layers.Dense(input_dims, activation='sigmoid')(x)


    decoder = keras.models.Model(latent_inputs, outputs, name='decoder')

    auto = keras.models.Model(
        inputs, decoder(encoder(inputs)[0]), name='autoencoder')

    auto.compile(optimizer='adam', loss='binary_crossentropy')
    
    return encoder, decoder, auto
