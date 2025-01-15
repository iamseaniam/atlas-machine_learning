#!/usr/bin/env python3
"""documentation"""
import numpy as np
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    """Documentation"""
    total_rewards = []

    for episode in range(episodes):
        state = env.reset()
        episode_reward = 0

        for step in range(max_steps):
            action = epsilon_greedy(Q, state, epsilon)
            result = env.step(action)
            new_state, reward, done = result[0], result[1], result[2]

            if done and reward == 0:
                reward = -1

            Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])
            state = new_state
            episode_reward += reward

            if done:
                break

        epsilon = max(min_epsilon, epsilon * (1 - epsilon_decay))
        total_rewards.append(episode_reward)

    return Q, total_rewards