#!/usr/bin/env python3
"""documentation"""
import numpy as np


def uni_bleu(references, sentence):
    """Documentation"""
    reference_words = {word for ref in references for word in ref}

    matches = sum(1 for word in sentence if word in reference_words)

    precision = matches / len(sentence) if len(sentence) > 0 else 0

    reference_lengths = [len(ref) for ref in references]
    closest_ref_len = min(
        reference_lengths,
        key=lambda ref_len: (abs(ref_len - len(sentence)), ref_len))
    if len(sentence) > closest_ref_len:
        brevity_penalty = 1
    else:
        brevity_penalty = np.exp(
            1 - closest_ref_len / len(sentence)) if len(sentence) > 0 else 0

    bleu_score = brevity_penalty * precision

    return bleu_score
