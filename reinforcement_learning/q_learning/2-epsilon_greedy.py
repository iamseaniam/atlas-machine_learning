#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """Documentation"""
    p = np.random.uniform(0,1) # numbers between 1 and 0

    if p < epsilon:
        # ! (Q.shape[1]) is grabbing column ie possible action
        # then whatever number it got it chooses a random number 0 - number
        action = np.random.randint(Q.shape[1])
    else:
        # ! (Q[state]) is grabbing  row ie the current state
        # then finds highest q-value for that state
        action = np.argmax(Q[state])
    return action
