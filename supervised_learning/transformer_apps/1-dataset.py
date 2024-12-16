#!/usr/bin/env python3
"""Documentation"""
# https://huggingface.co/learn/nlp-course/en/chapter2/4
import transformers
import tensorflow_datasets as tfds
import numpy as np
import tensorflow as tf


class Dataset:
    """Documentation"""

    def __init__(self):
        """Documentation"""

        self.data_train = tfds.load(
            "ted_hrlr_translate/pt_to_en", split="train", as_supervised=True
        )
        self.data_valid = tfds.load(
            "ted_hrlr_translate/pt_to_en",
            split="validation", as_supervised=True
        )

        self.pt_tokenizer, self.en_tokenizer = self.tokenize_dataset(
            self.data_train)

    def tokenize_dataset(self, data):
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

        pt_tokenizer = transformers.BertTokenizerFast.from_pretrained(
            "neuralmind/bert-base-portuguese-cased"
        )
        en_tokenizer = transformers.BertTokenizerFast.from_pretrained(
            "bert-base-uncased"
        )

        vocab_size = 2**13

        en_model_trained = en_tokenizer.train_new_from_iterator(
            text_iterator=en_iterator(), vocab_size=vocab_size
        )

        pt_model_trained = pt_tokenizer.train_new_from_iterator(
            text_iterator=pt_iterator(), vocab_size=vocab_size
        )

        return pt_model_trained, en_model_trained

    def encode(self, pt, en):
        """Documentation"""
        pt_tokens = self.pt_tokenizer.encode(pt.numpy().decode('utf-8'))
        en_tokens = self.en_tokenizer.encode(en.numpy().decode('utf-8'))

        start_token_pt = self.pt_tokenizer.vocab_size
        end_token_pt = self.pt_tokenizer.vocab_size + 1
        
        pt_tokens = [start_token_pt] + pt_tokens + [end_token_pt]
        
        start_token_en = self.en_tokenizer.vocab_size
        end_token_en = self.en_tokenizer.vocab_size + 1
        
        en_tokens = [start_token_en] + en_tokens + [end_token_en]

        pt_tokens = np.array(pt_tokens, dtype=np.int32)
        en_tokens = np.array(en_tokens, dtype=np.int32)

        return pt_tokens, en_tokens
