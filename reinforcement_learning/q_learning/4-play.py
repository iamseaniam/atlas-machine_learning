#!/usr/bin/env python3
"""documentation"""
import numpy as np

def play(env, Q, max_steps=100):
    """Plays an episode using the trained Q-table"""
    rendered_output = []
    total_reward = 0

    state = env.reset()[0]
    rendered_output.append(env.render())

    terminated, truncated = False, False
    step_counter = 0

    while not terminated and not truncated:
        action = np.argmax(Q[state, :])

        new_state, reward, terminated, truncated, _ = env.step(action)

        step_counter += 1

        state = new_state

        rendered_output.append(env.render())

        if step_counter >= max_steps:
            break

    env.close()

    return reward, rendered_output
