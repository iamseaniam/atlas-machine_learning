#!/usr/bin/env python3
"""documentation"""
from collections import Counter


def ngram_bleu(references, sentence, n):
    """Documentation"""
    def generate_ngrams(sequence, n):
        """Helper function to generate n-grams from a sequence of words."""
        return [tuple(
            sequence[i:i + n]) for i in range(len(sequence) - n + 1)]

    sentence_ngrams = generate_ngrams(sentence, n)
    sentence_counts = Counter(sentence_ngrams)

    reference_counts = Counter()
    for ref in references:
        ref_ngrams = generate_ngrams(ref, n)
        reference_counts.update(Counter(ref_ngrams))

    clipped_counts = {ngram: min(
        count,
        reference_counts[ngram]) for ngram, count in sentence_counts.items()}
    clipped_total = sum(clipped_counts.values())
    total_ngrams = len(sentence_ngrams)

    if total_ngrams == 0:
        return 0.0

    precision = clipped_total / total_ngrams

    sentence_length = len(sentence)
    reference_lengths = [len(ref) for ref in references]
    closest_ref_length = min(
        reference_lengths,
        key=lambda ref_len: (abs(ref_len - sentence_length), ref_len))

    if sentence_length > closest_ref_length:
        brevity_penalty = 1
    else:
        brevity_penalty = pow(
            2.718281828459045, 1 - closest_ref_length / sentence_length)

    return brevity_penalty * precision
