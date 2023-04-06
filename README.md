# Udacity Deep Reinforcement Learning: Project 1 Banana Navigator
First project of Udacity's Deep Reinforcement Learning, Banana Collector.
The project goal is to create an agent that can maximize the score on the Banana Navigator unity enviroment, (`UnityEnvironment(file_name="/data/Banana_Linux_NoVis/Banana.x86_64"`)

## Enviroment Details:


A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

0 - move forward.
1 - move backward.
2 - turn left.
3 - turn right.
The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.


## Instructions

To use test the agent with pretrained weights run `agent_act.py` or go thorugh the `agent_act.ipyn` .
The `model.pth` contains pretained weights for the model.

Follow the instructions in `Train.ipynb` to train a new agent and save new weights. 


### File Description

`Report.ipynb`: Contains the report of the process used to train the agent.

`model.py`: The DQN pytorch model definition.

`agent.py`: Contains the Agent class that can learn and interact with an environment state, and the ReplayBuffer class used to train the agent. 

`Train.ipynb`: Notebook used to bootstrap the environemnt and train the agent.

`Agent_Act.ipynb.ipynb`: Notebook to test the agent by using pretrained weights. (agent_act.py) is the python version.
