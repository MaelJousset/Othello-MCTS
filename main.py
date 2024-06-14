# # main.py
# import gymnasium as gym
# from mcts.node import Node
# from mcts.mcts import simple_mcts
# from othello.othello_state import OthelloState

# print("Starting the environment")
# # Instantiate the environment
# env = gym.make("ALE/Othello-v5", render_mode='rgb_array')

# print("Creating initial state")
# # Create initial state
# initial_state = OthelloState(env)

# print("Creating root node")
# # Create root node
# root = Node(initial_state)

# # Define the time limit in seconds
# time_limit_seconds = 1  # Start with 1 second for testing

# print("Performing MCTS")
# # Perform MCTS with a time limit
# best_node = simple_mcts(root, time_limit_seconds)

# print("Best node found, taking action")
# # Take the action leading to the best node
# action = best_node.action
# env.step(action)

# print("Finished")



# main.py
import gymnasium as gym
from mcts.node import Node
from mcts.mcts import mcts
from othello.othello_state import OthelloState

print("Starting the environment")
# Instantiate the environment
env = gym.make("ALE/Othello-v5", render_mode='rgb_array')

print("Creating initial state")
# Create initial state
initial_state = OthelloState(env)

print("Creating root node")
# Create root node
root = Node(initial_state)

# Define the time limit in seconds
time_limit_seconds = 1  # Start with 1 second for testing

print("Performing MCTS")
# Perform MCTS with a time limit
best_node = mcts(root, time_limit_seconds)

print("Best node found, taking action")
# Take the action leading to the best node
action = best_node.action
env.step(action)

print("Finished")
