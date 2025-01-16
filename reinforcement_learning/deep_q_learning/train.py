from breakout import *
import os
import torch
from PIL import Image
import numpy as np
import gymnasium as gym
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

enviroment = DQNBreakout(device=device, render_mode='human')

state = enviroment.reset()

for _ in range(100):
    action = enviroment.action_space.sample()

    state, reward, done, info = enviroment.step(action)
    # ! dum error, it was numpy verison issue
