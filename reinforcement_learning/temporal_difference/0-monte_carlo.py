#!/usr/bin/env python3
"""Docuentation for monte_carlo.py"""

import numpy as np


def monte_carlo(env, V, policy, episodes=5000,
                max_steps=100, alpha=0.1, gamma=0.99
                ):
    """Function that performs Monte Carlo algorithm"""
    for episodes in range(episodes):
        state = env.reset()
        episode_data = []  # storing (state, reward)

        for step in range(max_steps):
            action = policy(state)  # choosing action using policy
            next_state, reward, done, _ = env.step(action)  # taking action
            episode_data.append((state, reward))  # recording (state, reward)

            if done:
                break

            state = next_state

        G = 0  # initalize the return
        # in mont carlo reutrns (G) are calculated backwards

        # range(start, stop, step)
        # starts loop from last index of episode_data
        # stops loop before reaching -1, end of index
        # makes loop step backwards
        for t in range(len(episode_data) - 1, -1, -1):
            state, reward = episode_data[t]
            G = reward + gamma * G  # compute return

            # update value function using incremtal forula
            # V(S_t) <- V(S_t) + a[G_t - V(S_t)]
            V[state] += alpha * (G - V[state])

    return V
