#!/usr/bin/env python3
"""Documentation"""
import tensorflow.keras as keras


def autoencoder(input_dims, filters, latent_dims):
    encoder_input = keras.layers.Input(shape=input_dims)
    x = encoder_input

    for num_filters in filters:
        x = keras.layers.Conv2D(num_filters,
                                kernel_size=(3, 3),
                                padding='same',
                                activation='relu')(x)
        x = keras.layers.MaxPooling2D(pool_size=(2, 2))(x)

    latent_space = keras.layers.Conv2D(latent_dims[2],
                                       kernel_size=(3, 3),
                                       padding='same',
                                       activation='relu')(x)

    encoder = keras.models.Model(encoder_input, latent_space, name='encoder')

    decoder_input = keras.layers.Input(shape=latent_dims)
    x = decoder_input

    for num_filters in reversed(filters[:-1]):
        x = keras.layers.Conv2D(num_filters,
                                kernel_size=(3, 3),
                                padding='same',
                                activation='relu')(x)
        x = keras.layers.UpSampling2D(size=(2, 2))(x)

    x = keras.layers.Conv2D(filters[-1],
                            kernel_size=(3, 3),
                            padding='valid',
                            activation='relu')(x)

    decoder_output = keras.layers.Conv2D(input_dims[2],
                                         kernel_size=(3, 3),
                                         padding='same',
                                         activation='sigmoid')(x)

    decoder = keras.models.Model(decoder_input, decoder_output, name='decoder')

    auto_input = keras.layers.Input(shape=input_dims)
    encoded = encoder(auto_input)
    decoded = decoder(encoded)

    auto = keras.models.Model(auto_input, decoded, name='autoencoder')

    auto.compile(optimizer='adam', loss='binary_crossentropy')

    return encoder, decoder, auto
