#!/usr/bin/env python3
"""Documention"""
import numpy as np


def q_init(env):
    """Documentatiokn"""
    # print(env.observation_space) helped with understanding what its giving
    # print(env.action_space)
    # help(env.observation_space)

    # .n is an attribute that gives you total number of states/ actions
    q_table = np.zeros((env.observation_space.n, env.action_space.n))
    return q_table
