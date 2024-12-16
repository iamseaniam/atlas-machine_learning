#!/usr/bin/env python3
"""Documentation"""
# https://huggingface.co/learn/nlp-course/en/chapter2/4
import transformers
import tensorflow_datasets as tfds


class Dataset:
    """Documentation"""

    def __init__(self):
        """Documentation"""

        self.data_train = tfds.load(
            "ted_hrlr_translate/pt_to_en", split="train", as_supervised=True
        )
        self.data_valid = tfds.load(
            "ted_hrlr_translate/pt_to_en",
            split='validation', as_supervised=True
        )

        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)

    def tokenize_data(self, data):
        """Documentation"""

        en_base = []
        pt_base = []

        for en, pt in data:
            en_base.append(en.numpy().decode("utf-8"))
            pt_base.append(pt.numpy().decode("utf-8"))

        def en_iterator():
            """documentation"""
            yield from en_base

        def pt_iterator():
            """documentation"""
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

        return en_model_trained, pt_model_trained
