#!/usr/bin/env python3
"""dsijdsodjsd"""
import tensorflow as tf


def gensim_to_keras(model):
    """sodsdos"""
    weights = model.wv.vectors

    vocab_size, vector_size = weights.shape

    initial_weights = tf.convert_to_tensor(weights, dtype=tf.float32)

    embedding_layer = tf.keras.layers.Embedding(
        input_dim=vocab_size,
        output_dim=vector_size,
        embeddings_initializer=tf.keras.initializers.Constant(initial_weights),
        trainable=True
    )

    return embedding_layer
