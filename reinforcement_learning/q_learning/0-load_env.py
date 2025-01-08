#!/usr/bin/env python3
"""documentation"""
import gymnasium as gym
# from gymnasium.envs.toy_text im port frozen_lake

# ! is it just making an enviroment?
# ! all i am finding is stuff to do with the agent. 
# CONFUSEd
def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """Documentation"""

    # help(frozen_lake)
    # ? i dont understant, just because i am using the module it then allowed me to make custom enviroment
    evn = gym.make('FrozenLake-v1',
                   desc=desc,
                   map_name=map_name,
                   is_slippery=True
                   )

    return evn
