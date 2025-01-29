#!/usr/bin/env python3
""" TD(λ)"""
import numpy as np


def td_lambtha(env, V, policy, lambtha, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):
    """documentation"""
    for episode in range(episodes):
        state, _ = env.reset()
        if isinstance(state, tuple):
            state = state[0]
        eligibility = np.zeros_like(V)

        for step in range(max_steps):
            action = policy(state)

            next_state, reward, terminated, truncated, _ = env.step(action)

            done = terminated or truncated

            td_error = reward + gamma * V[next_state] - V[state]

            eligibility[state] += 1

            V += alpha * td_error * eligibility

            eligibility *= gamma * lambtha

            state = next_state

            if done:
                break

    return V
