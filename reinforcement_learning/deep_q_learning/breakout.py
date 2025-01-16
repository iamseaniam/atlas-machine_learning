import collections
import cv2
import gym
import numpy as np
from PIL import Image
import torch


class DQNBreakout(gym.Wrapper):

    def __init__(self, render_mode='rgb_array', repeat=4, device='cpu'):
        env = gym.make('BreakoutNoFrameskip-v4', render_mode=render_mode)
        # // add celeste to playstation wishlist

        super(DQNBreakout, self).__init__(env)

        self.image_shape = (84, 84)  # 84 by 84 images
        self.repeat = repeat
        self.lives = env.unwrapped.ale.lives()
        self.frame_buffer = []
        self.device = device

    def step(self, action):
        total_reward = 0
        done = False

        for i in range(self.repeat):
            observation, reward, done, truncated, info = self.env.step(action)

            total_reward += reward

            current_lives = info['lives']

            if current_lives < self.lives:
                total_reward = total_reward - 1  # ! Penalize the agent for losing a life
                self.lives = current_lives

            # // print(f"Lives: {self.lives} Total Reward: {total_reward}")

            self.frame_buffer.append(observation)

            if done:
                break

        max_frame = np.max(self.frame_buffer[-2:], axis=0)
        # // max_frame = max_frame.to(self.device)
        max_frame = self.process_observation(max_frame)
        max_frame = max_frame.to(self.device)

        total_reward = torch.tensor(total_reward).view(1, -1).float()
        # saying to.device is sending it to cpu or gpu
        total_reward = total_reward.to(self.device)

        done = torch.tensor(done).view(1, -1)
        done = done.to(self.device)

        return max_frame, total_reward, done, info

    def reset(self):
        self.frame_buffer = []

        observation, _ = self.env.reset()

        self.lives = self.env.ale.lives()

        observation = self.process_observation(observation)

        return observation

    def process_observation(self, observation):

        ing = Image.fromarray(observation)
        ing = ing.resize(self.image_shape)  # resize the image
        ing = ing.convert('L')  # convert the image to grayscale
        ing = np.array(ing)
        ing = torch.from_numpy(ing)
        ing = ing.unsqueeze(0)
        ing = ing.unsqueeze(0)
        ing = ing / 255.0  # normalize the image between 0 and 1

        ing - ing.to(self.device)

        return ing
