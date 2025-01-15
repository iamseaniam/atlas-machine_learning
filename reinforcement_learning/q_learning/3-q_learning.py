#!/usr/bin/env python3
"""documentation"""
import numpy as np
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    """Documentation"""
    rewards_per_episode = np.zeros(episodes)

    for i in range(episodes):
        state = env.reset()[0]
        terminated = False
        truncated = False
        step_counter = 0

        while not terminated and not truncated:
            action = epsilon_greedy(Q, state, epsilon)

            new_state, reward, terminated, truncated, _ = env.step(action)

            Q[state, action] = Q[state, action] + alpha * (
                reward + gamma * np.max(Q[new_state, :]) - Q[state, action]
            )

            step_counter += 1
            state = new_state

            if step_counter >= max_steps:
                break

        epsilon = max(epsilon - epsilon_decay, 0)

        if epsilon == 0:
            alpha = min_epsilon

        if reward == 1:
            rewards_per_episode[i] = 1
        elif truncated or terminated:
            rewards_per_episode[i] = -1

    env.close()

    return Q, rewards_per_episode
