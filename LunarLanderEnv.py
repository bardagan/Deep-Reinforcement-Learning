import gym
from gym import spaces
import numpy as np
import matplotlib.pyplot as plt
from gym.wrappers import Monitor


# class MyLunarLanderEnv_Monitored(gym.Env):
#     def __init__(self, video_folder):
#         self.env = gym.make('LunarLanderContinuous-v2')
#         self.video_folder = video_folder
#         self.env = Monitor(self.env, self.video_folder, force=True)
#         self.observation_space = self.env.observation_space
#         self.action_space = spaces.Discrete(8)
#         # Nop, fire left engine, main engine, right engine
#         self.action_map = {
#             0: (-1, 0), # nop
#             1: (-1 , -1), # fire left engine - strong
#             2: (1, 0), # fire main engine - strong
#             3: (-1 , 1), # fire right engine - strong
#             4: (-1 , -0.6), # fire left engine - weak
#             5: (0.1, 0), # fire main engine - weak
#             6: (-1 , 0.6), # fire right engine - weak
#             7: (0.5, 0) # fire main engine - medium
#         }

#     def reset(self):
#         self.env.close()
#         self.env = Monitor(self.env, self.video_folder, resume=True)
#         return self.env.reset()

#     def step(self, action):
#         return self.env.step(self.action_map[action])

class MyLunarLanderEnv(gym.Env):
    def __init__(self):
        self.env = gym.make('LunarLanderContinuous-v2')
        
        self.observation_space = self.env.observation_space
        self.action_space = spaces.Discrete(8)
        # Nop, fire left engine, main engine, right engine
        self.action_map = {
            0: (-1, 0), # nop
            1: (-1 , -1), # fire left engine - strong
            2: (1, 0), # fire main engine - strong
            3: (-1 , 1), # fire right engine - strong
            4: (-1 , -0.6), # fire left engine - weak
            5: (0.1, 0), # fire main engine - weak
            6: (-1 , 0.6), # fire right engine - weak
            7: (0.5, 0) # fire main engine - medium
        }

    def reset(self):
        return self.env.reset()

    def step(self, action):
        return self.env.step(self.action_map[action])
