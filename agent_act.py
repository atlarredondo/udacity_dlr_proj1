#!/usr/bin/env python
# coding: utf-8

# # Navigation
# 
# ---
# 
# In this notebook, the agent acts with trained weights from the  [Deep Reinforcement Learning Nanodegree](https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893).
# 
# ### 1. Start the Environment
# 
# We begin by importing some necessary packages.  If the code cell below returns an error, please revisit the project instructions to double-check that you have installed [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation.md) and [NumPy](http://www.numpy.org/).

# In[1]:


from unityagents import UnityEnvironment
import numpy as np


# In[2]:


env = UnityEnvironment(file_name="Banana.app")


# In[3]:


# get the default brain
brain_name = env.brain_names[0]
brain = env.brains[brain_name]


# In[6]:


# Initializing agent with pretained weights.
import torch

from agent import Agent

agent = Agent(state_size=37, action_size=4, seed=0)
agent.qnetwork_local.load_state_dict(torch.load('model.pth' ,map_location='cpu'))


# In[10]:


env_info = env.reset(train_mode=False)[brain_name] # reset the environment
state = env_info.vector_observations[0]            # get the current state
score = 0                                          # initialize the score
while True:
    action = agent.act(state)                      # select an action
    env_info = env.step(action)[brain_name]        # send the action to the environment
    next_state = env_info.vector_observations[0]   # get the next state
    reward = env_info.rewards[0]                   # get the reward
    done = env_info.local_done[0]                  # see if episode has finished
    score += reward                                # update the score
    state = next_state                             # roll over the state to next time step
    if done:                                       # exit loop if episode finished
        break
    
print("Score: {}".format(score))


# When finished, you can close the environment.

# In[11]:


env.close()

