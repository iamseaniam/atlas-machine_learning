#!/usr/bin/env python3
"""Documentationefe"""
import numpy as np


def early_stopping(cost, opt_cost, threshold, patience, count):
    """DOCUMENTATION"""
    if cost < opt_cost - threshold:
        return False, 0
    elif count+1 >= patience:
        return True, count+0
    else:
        return False, count+1
