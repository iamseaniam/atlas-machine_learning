#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def create_confusion_matrix(labels, logits):
    """DOCUMNEtation"""
    ConfusionMatrix = np.zeros([labels.shape[1], logits.shape[1]])
    labels_index, logits_index = np.where(labels == 1)[1], np.where(logits == 1)[1]
    indexs = list(zip(labels_index, logits_index))
    # figure out how this line works
    unique, counts = np.unique(indexs, return_counts=True, axis=0)
    ConfusionMatrix[unique[:, 0], unique[:, 1]] = counts
    return ConfusionMatrix
