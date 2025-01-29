#!/usr/bin/env python3
"""Docuentation for monte_carlo.py"""

import numpy as np
# 2:28pm 1/28/25 CODE does not look like expected output ):
# 2:31 1/28/25 CODE just ouputs a 8x8 array of ones

# * move all comments
# ! TypeError: unsupported operand type(s) for %: 'tuple' and 'int'
# # hopefully this will fix this error
# range(start, stop, step)
# starts loop from last index of episode_data
# stops loop before reaching -1, end of index
# makes loop step backwards
# in mont carlo reutrns (G) are calculated backwards
# update value function using incremtal forula
# V(S_t) <- V(S_t) + a[G_t - V(S_t)]


def monte_carlo(env, V, policy, episodes=5000,
                max_steps=100, alpha=0.1, gamma=0.99
                ):
    """Function that performs Monte Carlo algorithm"""
    num_states = env.observation_space.n
    returns = {s: [] for s in range(num_states)}

    for episodes in range(episodes):
        state, _ = env.reset()
        episode_data = []  # storing (state, reward)
        for step in range(max_steps):
            if isinstance(state, tuple):
                state = state[0]  # Extract integer if state is a tuple
            action = policy(state)  # choosing action using policy
            next_state, reward, terminated, truncated, _ = env.step(
                action)  # taking action
            done = terminated or truncated
            episode_data.append((state, reward))  # recording (state, reward)
            state = next_state
            if done:
                break

        G = 0  # initalize the return
        for g_state, reward in reversed(episode_data):
            G = gamma * G + reward  # compute return

            returns[g_state].append(G)  # store return

            V[state] += alpha * np.mean(returns[g_state])

    return V
