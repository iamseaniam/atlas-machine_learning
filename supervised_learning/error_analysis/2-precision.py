#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def precision(confusion):
    """DOCUMNEtation"""
    SUMMMMMMMMM = np.sum(confusion, axis=0)
    truePositive = np.diag(confusion)
    falsePositive = SUMMMMMMMMM - truePositive
    return truePositive / (truePositive + falsePositive)
