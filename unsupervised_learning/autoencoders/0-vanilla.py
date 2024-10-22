#!/usr/bin/env python3
"""Documentation"""
import tensorflow.keras as keras


def build_encoder(input_dim, hidden_layer, latent_dims):
    """Documentation"""
    input = keras.layers.Input(shape=(input_dims,))
    x = inputs

    # hl: Add hidden layers
    for nodes in hidden_layer:
        x = keras.layers.Dense(nodes, activation='relu')(x)

    # hl: latent space 
    latent = keras.layers.Dense(latent_dims, activations='relu')(x)

    encoder = keras.models.Model(inputs, latent, name='encoder')
    return encoder

def build_decoder(latent_dims, hidden_layers, input_dims):
    """Documentation"""
    latent_inputs = keras.layers.Input(shape=(latent_dims,))
    x = latent_inputs

    # hl: Reverse the hidden layers for the decoder
    for nodes in reversed(hidden_layers):
        x = keras.layers.Dense(nodes, activation='relu')(x)

    # hl: Output layer should match the original input dimensions
    outputs = keras.layers.Dense(input_dims, activations='sigmoid')(x)

    decoder = keras.models.Model(latent_inputs, outputs, name='decoder')
    return decoder

def autoencoder(input_dims, hidden_layers, latent_dims):
    """Documentation"""
    auto_input = encoder.input
    auto_output = decoder(encoder(auto_input))

    auto = models.Model(auto_input, auto_output, name='autoencoder')
    return auto
