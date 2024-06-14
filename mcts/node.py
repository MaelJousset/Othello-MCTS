# # mcts/node.py
# import numpy as np

# class Node:
#     def __init__(self, state, parent=None, action=None):
#         self.state = state
#         self.parent = parent
#         self.children = []
#         self.visits = 0
#         self.total_reward = 0
#         self.action = action  # Track the action leading to this node

#     def is_fully_expanded(self):
#         return len(self.children) == len(self.state.available_actions())

#     def best_child(self, c_param=1.4):
#         choices_weights = [
#             (child.total_reward / child.visits) + c_param * (np.sqrt((2 * np.log(self.visits) / child.visits)))
#             for child in self.children
#         ]
#         return self.children[np.argmax(choices_weights)]


# mcts/node.py
import math
import random

class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.total_reward = 0
        self.action = action

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.available_actions())

    def best_child(self, c_param=1.4):
        choices_weights = [
            (child.total_reward / child.visits) + c_param * math.sqrt((2 * math.log(self.visits) / child.visits))
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

    def expand(self):
        tried_actions = [child.action for child in self.children]
        available_actions = [action for action in self.state.available_actions() if action not in tried_actions]
        action = random.choice(available_actions)
        next_state, action = self.state.next_state(action)
        child_node = Node(next_state, parent=self, action=action)
        self.children.append(child_node)
        return child_node
