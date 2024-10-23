#!/usr/bin/env python3
"""Documentation"""
import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims, lambtha):
    """Documentation"""
    encoder_input = keras.layers.Input(shape=(input_dims,))
    x = encoder_input

    for nodes in hidden_layers:
        x = keras.layers.Dense(nodes, activation='relu')(x)

    latent_space = keras.layers.Dense(latent_dims,
                                      activation='relu',
                                      activity_regularizer=keras.regularizers.l1(lambtha))(x)

    encoder = keras.models.Model(encoder_input, latent_space, name='encoder')

    decoder_input = keras.layers.Input(shape=(latent_dims,))
    x = decoder_input

    for nodes in reversed(hidden_layers):
        x = keras.layers.Dense(nodes, activation='relu')(x)

    decoder_output = keras.layers.Dense(input_dims, activation='sigmoid')(x)

    decoder = keras.models.Model(decoder_input, decoder_output, name='decoder')

    auto_input = keras.layers.Input(shape=(input_dims,))
    encoded = encoder(auto_input)
    decoded = decoder(encoded)

    auto = keras.models.Model(auto_input, decoded, name='sparse_autoencoder')

    auto.compile(optimizer='adam', loss='binary_crossentropy')

    return encoder, decoder, auto
