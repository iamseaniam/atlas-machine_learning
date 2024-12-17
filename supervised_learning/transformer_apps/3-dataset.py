#!/usr/bin/env python3
"""Documentation"""
# https://huggingface.co/learn/nlp-course/en/chapter2/4
import tensorflow_datasets as tfds
import transformers
import tensorflow as tf


class Dataset:
    """Documentation"""

    def __init__(self, batch_size, max_len):
        """Documentation"""

        self.data_train = tfds.load(
            "ted_hrlr_translate/pt_to_en", split="train", as_supervised=True
        )
        self.data_valid = tfds.load(
            "ted_hrlr_translate/pt_to_en",
            split="validation", as_supervised=True
        )

        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)

        self.data_train = self.data_train.map(self.tf_encode)
        self.data_train = self.data_train.filter(
            lambda pt,
            en: tf.logical_and(tf.size(pt) <= max_len, tf.size(en) <= max_len))
        self.data_train = self.data_train.cache()
        self.data_train = self.data_train.shuffle(buffer_size=20000)
        self.data_train = self.data_train.padded_batch(
            batch_size, padded_shapes=([None], [None]))
        self.data_train = self.data_train.prefetch(
            buffer_size=tf.data.experimental.AUTOTUNE)

        self.data_valid = self.data_valid.map(self.tf_encode)
        self.data_valid = self.data_valid.filter(
            lambda pt,
            en: tf.logical_and(tf.size(pt) <= max_len, tf.size(en) <= max_len))
        self.data_valid = self.data_valid.padded_batch(
            batch_size, padded_shapes=([None], [None]))

    def tokenize_dataset(self, data):
        """documentation"""

        en_base = []
        pt_base = []

        for pt, en in data:
            pt_base.append(pt.numpy().decode("utf-8"))
            en_base.append(en.numpy().decode("utf-8"))

        def en_iterator():
            """Yields English sentences"""
            yield from en_base

        def pt_iterator():
            """Yields Portuguese sentences"""
            yield from pt_base

        tokenizer_pt = transformers.BertTokenizerFast.from_pretrained(
            "neuralmind/bert-base-portuguese-cased"
        )
        tokenizer_en = transformers.BertTokenizerFast.from_pretrained(
            "bert-base-uncased"
        )

        vocab_size = 2**13

        en_model_trained = tokenizer_en.train_new_from_iterator(
            text_iterator=en_iterator(), vocab_size=vocab_size
        )

        pt_model_trained = tokenizer_pt.train_new_from_iterator(
            text_iterator=pt_iterator(), vocab_size=vocab_size
        )

        return pt_model_trained, en_model_trained

    def encode(self, pt, en):
        """Encode Portuguese and English sentences into token IDs"""

        pt_tokens = self.tokenizer_pt.encode(pt.numpy().decode("utf-8"))
        en_tokens = self.tokenizer_en.encode(en.numpy().decode("utf-8"))

        pt_tokens = [
            self.tokenizer_pt.vocab_size, *pt_tokens, 
            self.tokenizer_pt.vocab_size + 1
        ]
        en_tokens = [
            self.tokenizer_en.vocab_size, *en_tokens, 
            self.tokenizer_en.vocab_size + 1
        ]

        return pt_tokens, en_tokens

    def tf_encode(self, pt, en):
        """Apply encoding to the dataset using TensorFlow functions"""

        pt_tokens, en_tokens = tf.py_function(
            func=self.encode, 
            inp=[pt, en], 
            Tout=[tf.int64, tf.int64]
        )

        pt_tokens.set_shape([None])
        en_tokens.set_shape([None])

        return pt_tokens, en_tokens
