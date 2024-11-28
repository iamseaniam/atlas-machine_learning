#!/usr/bin/env python3
"""documentation"""
from collections import Counter
from math import exp


def cumulative_bleu(references, sentence, n):
    """Documentation"""
    def generate_ngrams(sequence, n):
        """Helper function to generate n-grams from a sequence of words."""
        return [tuple(sequence[i:i + n]) for i in range(len(sequence) - n + 1)]

    def ngram_precision(references, sentence, n):
        """Calculates the n-gram precision for a specific n."""
        sentence_ngrams = generate_ngrams(sentence, n)
        sentence_counts = Counter(sentence_ngrams)

        reference_counts = Counter()
        for ref in references:
            ref_ngrams = generate_ngrams(ref, n)
            reference_counts.update(Counter(ref_ngrams))

        clipped_counts = {
            ngram: min(
                count,
                reference_counts[ngram]
                ) for ngram, count in sentence_counts.items()}
        clipped_total = sum(clipped_counts.values())
        total_ngrams = len(sentence_ngrams)

        if total_ngrams == 0:
            return 0.0

        return clipped_total / total_ngrams

    precisions = [ngram_precision(
        references, sentence, i) for i in range(1, n + 1)]

    sentence_length = len(sentence)
    reference_lengths = [len(ref) for ref in references]
    closest_ref_length = min(
        reference_lengths,
        key=lambda ref_len: (abs(ref_len - sentence_length), ref_len))

    if sentence_length > closest_ref_length:
        brevity_penalty = 1
    else:
        brevity_penalty = exp(1 - closest_ref_length / sentence_length)

    geometric_mean = (sum(map(
        lambda x: x if x > 0 else 0,
        precisions)) / n) if all(precisions) else 0

    return brevity_penalty * geometric_mean
