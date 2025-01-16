#!/usr/bin/env python3
"""documentation"""
import gym


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """ Makes custom environment for agent to use.

    Args:
        desc: the param to specify non preloaded maps
        map_name: the id to preloaded maps
        is_slippery: Is the param that makes the map slippy, or not

    Returns:
        env: the custom environment
    """
    env = gym.make('FrozenLake-v1',
                   desc=desc,
                   map_name=map_name,
                   is_slippery=is_slippery,
                   render_mode="ansi"  # ! Add render_mode="ansi"
                   )

    return env
