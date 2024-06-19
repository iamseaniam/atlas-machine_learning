#!/usr/bin/env python3
"""Documentation"""
import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """DOCUMNEtation"""
    TrueP = np.diag(confusion)
    FalseP = np.sum(confusion, axis=0) - TrueP
    FalseN = np.sum(confusion, axis=1) - TrueP
    precisions = precision(confusion)
    RecallPotion = TrueP / (TrueP + FalseN)
    return 2/((RecallPotion ** -1) + (precisions ** -1))
