#!/usr/bin/env python3
"""Documentation"""
import tensorflow.keras as keras


def sampling(args):
    """Reparameterization trick by sampling from an isotropic unit Gaussian."""
    z_mean, z_log_sigma = args
    batch = keras.backend.shape(z_mean)[0]
    dim = keras.backend.int_shape(z_mean)[1]
    epsilon = keras.backend.random_normal(shape=(batch, dim))
    return z_mean + keras.backend.exp(0.5 * z_log_sigma) * epsilon

def autoencoder(input_dims, hidden_layers, latent_dims):
    """Documentation"""
    encoder_input = keras.layers.Input(shape=(input_dims,))
    x = encoder_input
    for nodes in hidden_layers:
        x = keras.layers.Dense(nodes, activation='relu')(x)

    z_mean = keras.layers.Dense(latent_dims)(x)
    z_log_sigma = keras.layers.Dense(latent_dims)(x)

    z = keras.layers.Lambda(sampling, output_shape=(latent_dims,))([z_mean, z_log_sigma])

    encoder = keras.models.Model(encoder_input, [z, z_mean, z_log_sigma], name="encoder")

    decoder_input = keras.layers.Input(shape=(latent_dims,))
    x = decoder_input
    for nodes in reversed(hidden_layers):
        x = keras.layers.Dense(nodes, activation='relu')(x)
    decoder_output = keras.layers.Dense(input_dims, activation='sigmoid')(x)

    decoder = keras.models.Model(decoder_input, decoder_output, name="decoder")

    autoencoder_input = keras.layers.Input(shape=(input_dims,))
    z, z_mean, z_log_sigma = encoder(autoencoder_input)
    reconstructed = decoder(z)
    auto = keras.models.Model(autoencoder_input, reconstructed, name="autoencoder")

    def vae_loss(x, reconstructed_x):
        """Documentation"""
        reconstruction_loss = keras.losses.binary_crossentropy(x, reconstructed_x)
        reconstruction_loss *= input_dims
        kl_loss = 1 + z_log_sigma - keras.backend.square(z_mean) - keras.backend.exp(z_log_sigma)
        kl_loss = keras.backend.sum(kl_loss, axis=-1)
        kl_loss *= -0.5
        return keras.backend.mean(reconstruction_loss + kl_loss)

    auto.compile(optimizer=keras.optimizers.Adam(), loss=vae_loss)

    return encoder, decoder, auto
