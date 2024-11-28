#!/usr/bin/env python3
"""dsijdsodjsd"""
import gensim
import numpy as np


def tf_idf(sentences, vocab=None):
    """sodsdos"""
    tokenized_sentences = [
        sentence.lower().split() for sentence in sentences]

    if vocab is None:
        vocab = sorted(set(
            word for sentence in tokenized_sentences for word in sentence))
    else:
        vocab = sorted(vocab)

    word_to_index = {word: i for i, word in enumerate(vocab)}

    s = len(sentences)
    f = len(vocab)
    tf = np.zeros((s, f), dtype=float)

    for i, sentence in enumerate(tokenized_sentences):
        for word in sentence:
            if word in word_to_index:
                tf[i, word_to_index[word]] += 1
        if len(sentence) > 0:
            tf[i] /= len(sentence)

    df = np.zeros(f, dtype=float)
    for j, word in enumerate(vocab):
        df[j] = sum(1 for sentence in tokenized_sentences if word in sentence)

    idf = np.log((s / (df + 1)) + 1)

    embeddings = tf * idf

    return embeddings, vocab
