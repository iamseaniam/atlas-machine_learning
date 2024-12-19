#!/usr/bin/env python3
"""Documentation"""
import os
import numpy as np
import tensorflow_hub as hub


def load_corpus(corpus_path):
    """ Documentation """
    corpus = []
    for filename in os.listdir(corpus_path):
        file_path = os.path.join(corpus_path, filename)
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            with open(file_path, 'r', encoding='utf-8') as f:
                corpus.append(f.read())
    return corpus


def semantic_search(corpus_path, sentence):
    """ Documentation """
    corpus = load_corpus(corpus_path)

    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

    embeddings = embed(corpus + [sentence])
    corpus_embeddings = embeddings[:-1]
    query_embedding = embeddings[-1]

    cosine_similarities = np.inner(corpus_embeddings, query_embedding)

    most_similar_idx = np.argmax(cosine_similarities)

    return corpus[most_similar_idx]
