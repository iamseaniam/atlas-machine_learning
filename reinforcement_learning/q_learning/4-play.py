#!/usr/bin/env python3
"""documentation"""
import numpy as np


def play(env, Q, max_steps=100):
    """Plays an episode using the trained Q-table"""
    state = env.reset()
    total_reward = 0
    rendered_outputs = []

    for step in range(max_steps):
        action = np.argmax(Q[state, :])
        state, reward, done, _ = env.step(action)
        total_reward += reward

        # Render the current state of the environment
        rendered_outputs.append(env.render())

        if done:
            break

    # Ensure the final state is displayed
    rendered_outputs.append(env.render())
    
    return total_reward, rendered_outputs
