#!/usr/bin/env python3
"""Documentation"""
import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """Doumentation"""
    inputs = tensorflow.keras.Input(shape=(input_dims,))
    x = inputs
    for nodes in hidden_layers:
        x = tensorflow.keras.layers.Dense(nodes, activation='relu')(x)

    z_mean = tensorflow.keras.layers.Dense(latent_dims)(x)
    z_log_var = tensorflow.keras.layers.Dense(latent_dims)(x)

    def sampling(args):
        z_mean, z_log_var = args
        epsilon = tensorflow.keras.backend.random_normal(shape=tensorflow.keras.backend.shape(z_mean))
        return z_mean + tensorflow.keras.backend.exp(0.5 * z_log_var) * epsilon

    z = tensorflow.keras.layers.Lambda(sampling)([z_mean, z_log_var])

    encoder = tensorflow.keras.Model(inputs, [z, z_mean, z_log_var], name="encoder")

    latent_inputs = tensorflow.keras.Input(shape=(latent_dims,))
    x = latent_inputs
    for nodes in reversed(hidden_layers):
        x = tensorflow.keras.layers.Dense(nodes, activation='relu')(x)
    
    outputs = tensorflow.keras.layers.Dense(input_dims, activation='sigmoid')(x)
    decoder = tensorflow.keras.Model(latent_inputs, outputs, name="decoder")

    outputs = decoder(encoder(inputs)[0])
    auto = tensorflow.keras.Model(inputs, outputs, name="autoencoder")

    def vae_loss(y_true, y_pred):
        reconstruction_loss = tensorflow.keras.losses.binary_crossentropy(y_true, y_pred)
        reconstruction_loss *= input_dims
        kl_loss = -0.5 * tensorflow.keras.backend.sum(1 + z_log_var - tensorflow.keras.backend.square(z_mean) - tensorflow.keras.backend.exp(z_log_var), axis=-1)
        return tensorflow.keras.backend.mean(reconstruction_loss + kl_loss)

    auto.compile(optimizer=tensorflow.keras.optimizers.Adam(), loss=vae_loss)
    
    return encoder, decoder, auto
