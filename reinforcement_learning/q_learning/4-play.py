#!/usr/bin/env python3
"""documentation"""
import numpy as np


def play(env, Q, max_steps=100):
    """Plays an episode using the trained Q-table"""
    rendered_output = []
    total_reward = 0

    state = env.reset()[0]
    rendered_output.append(env.render(render_mode="ansi"))

    terminated, truncated = False, False
    step_counter = 0

    while not terminated and not truncated:
        action = np.argmax(Q[state, :])

        # i feel like i mess this line up, dumbo errors
        new_state, reward, terminated, truncated, _ = env.step(action)

        step_counter += 1
        total_reward += reward

        state = new_state

        rendered_output.append(env.render(render_mode="ansi"))

        if step_counter >= max_steps:
            break

    env.close()

    # seeing if chmod will help checker
    return total_reward, rendered_output
