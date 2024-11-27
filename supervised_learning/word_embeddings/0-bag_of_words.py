#!/usr/bin/env python3
"""dsijdsodjsd"""
import gensim
import numpy as np


def bag_of_words(sentences, vocab=None):
    """sodsdos"""
    tokenized_sentences = [sentence.lower().split() for sentence in sentences]

    if vocab is None:
        vocab = sorted(set(word for sentence in tokenized_sentences for word in sentence))
    else:
        vocab = sorted(vocab)

    word_to_index = {word: i for i, word in enumerate(vocab)}

    embeddings = np.zeros((len(sentences), len(vocab)), dtype=int)

    for i, sentence in enumerate(tokenized_sentences):
        for word in sentence:
            if word in word_to_index:
                embeddings[i, word_to_index[word]] += 1

    return embeddings, vocab

