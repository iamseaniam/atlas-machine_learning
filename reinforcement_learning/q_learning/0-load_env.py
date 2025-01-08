#!/usr/bin/env python3
"""documentation"""
import gymnasium as gym
# from gymnasium.envs.toy_text im port frozen_lake

# ! is it just making an enviroment?
# ! all i am finding is stuff to do with the agent.
# CONFUSEd


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """ Makes custotum enviroment for agent to use.

    Args:
        desc: the param to speficy non preloaded maps
        map_name: the id to preloaded maps
        is_slippery: Is the param that makes the map slippy, or not

    Returns:
        env: the custom enviroment
    """

    # ! to help me understand frozen lake
    # help(frozen_lake)

    # ? i dont understant,
    # ? just because i am using the module,
    # ? it then allowed me to make custom enviroment

    # just passing in the parameters to make function
    evn = gym.make('FrozenLake-v1',  # the module? Pretty sure
                   desc=desc, 
                   map_name=map_name,
                   is_slippery=is_slippery
                   )

    return evn
