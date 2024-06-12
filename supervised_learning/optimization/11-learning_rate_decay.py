#!/usr/bin/env python3
"""DOCUMENTATION"""
import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """DOCUMENTATION"""
    return alpha / (1 + (decay_rate * (global_step // decay_step)))
