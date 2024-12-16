#!/usr/bin/env python3
"""Documentation"""
import transformers
import tensorflow_datasets as tfds


class Dataset:
    """Documentation"""

    def __init__(self):
        """Documentation"""

        self.data_train = tfds.load(
            'ted_hrlr_translate/pt_to_en',
            split='train',
            as_supervised=True
            )

        self.data_valid = tfds.load(
            'ted_hrlr_translate/pt_to_en',
            split='validation',
            as_supervised=True
            )

        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)


    def tokenizse_dataset(self, data):
        """Documentation"""

        portuguese_base = []
        english_base = []

        for english, portuguese in data:
            english_base.append(
                english.numpy().decode(
                    "utf-8"
                    ))

            portuguese_base.append(
                portuguese.numpy().decode(
                    "utf-8"
                    ))

        def english_itorrater():
            for english in english_base:
                yield english

        def portuguese_iterator():
            for portuguese in portuguese_base:
                yield portuguese

        tokenizer_port = transformers.BertTokenizerFast.from_pretrained(
            "neuralmind/bert-base-portuguese-cased"
        )

        english_tokenizer = transformers.BertTokenizerFast.from_pretrained(
            "bert-base-uncased"
        )

        vocab_size = 2**13

        english_model_trained = english_tokenizer.train_new_from_iterator(
            text_iterator=english_itorrater(),
            vocab_size=vocab_size
        )
        portuguese_model_trained = tokenizer_port.train_new_from_iterator(
            text_iterator=portuguese_iterator(),
            vocab_size=vocab_size
        )

        return english_model_trained, portuguese_model_trained
