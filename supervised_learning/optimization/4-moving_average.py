#!/usr/bin/env python3
"""DOCUMENTATION"""
import numpy as np


def moving_average(data, beta):
    """DOCUMENTATION"""
    w_avg, w_avg_list = 0, []
    for i, x in enumerate(data):
        w_avg = (w_avg*beta) + (x*(1-beta))
        bias_correct = w_avg / (1 - (beta**(i+1)))
        w_avg_list.append(bias_correct)
    return w_avg_list
