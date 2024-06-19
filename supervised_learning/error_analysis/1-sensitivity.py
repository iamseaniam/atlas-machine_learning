#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def sensitivity(confusion):
    """DOCUMNEtation"""
    Summing = np.sum(confusion, axis=1)
    true_positive = np.diag(confusion)
    false_negitive = Summing - true_positive
    return true_positive / (true_positive + false_negitive)
