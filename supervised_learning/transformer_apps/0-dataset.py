#!/usr/bin/env python3
"""Documentation"""
import transformers
import tensorflow_datasets as tfds


class Dataset:
    """Documentation"""

    def __init__(self):
        """Documentation"""
        self.data_train = tfds.load('ted_hrlr_translate/pt_to_en', split='train', as_supervised=True)
        self.data_valid = tfds.load('ted_hrlr_translate/pt_to_en', split='validation', as_supervised=True)

        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(self.data_train)


    def tokenizse_dataset(self, data):
        """Documentation"""
        tokenizer_pt = transformers.BertTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
        tokenizer_en = transformers.BertTokenizer.from_pretrained("bert-base-uncased")

        portuguese_sentenes = []
        english_sentences = []
        for pt, en in data.take(10000):
            portuguese_sentenes.append(pt.numpy().decode('utf-8'))
            english_sentences.append(en.numpy().decode('utf-8'))

        tokenizer_pt = transformers.BertTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
        tokenizer_en = transformers.BertTokenizer.from_pretrained("bert-base-uncased")
            
        return tokenizer_pt, tokenizer_en
