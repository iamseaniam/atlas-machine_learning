#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def specificity(confusion):
    """DOCUMNEtation"""
    trueP = np.diag(confusion)
    FalseP = np.sum(confusion, axis=1) - trueP
    FalseN = np.sum(confusion, axis=0) - trueP
    TrueN = np.sum(confusion) - (trueP + FalseP + FalseN)
    return TrueN / (TrueN + FalseP)
