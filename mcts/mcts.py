# # mcts/simple_mcts.py
# import random
# import time
# from mcts.node import Node

# def simple_mcts(root, time_limit_seconds):
#     start_time = time.time()
    
#     while time.time() - start_time < time_limit_seconds:
#         node = simple_tree_policy(root)
#         reward = simple_default_policy(node.state)
#         simple_backup(node, reward)
    
#     return root.best_child(0)

# def simple_tree_policy(node):
#     while not node.state.is_terminal():
#         if not node.is_fully_expanded():
#             return simple_expand(node)
#         else:
#             node = node.best_child()
#     return node

# def simple_expand(node):
#     action = random.choice(node.state.available_actions())
#     new_state, action = node.state.next_state(action)
#     child_node = Node(new_state, parent=node, action=action)
#     node.children.append(child_node)
#     return child_node

# def simple_default_policy(state):
#     while not state.is_terminal():
#         action = random.choice(state.available_actions())
#         state, _ = state.next_state(action)
#     return state.reward()

# def simple_backup(node, reward):
#     while node is not None:
#         node.visits += 1
#         node.total_reward += reward
#         node = node.parent


# mcts/mcts.py
import random
import time
from mcts.node import Node

def mcts(root, time_limit_seconds):
    start_time = time.time()
    iterations = 0

    while time.time() - start_time < time_limit_seconds:
        iterations += 1
        node = tree_policy(root)
        reward = default_policy(node.state)
        backup(node, reward)

    print(f"Completed {iterations} iterations")
    return root.best_child(0)

def tree_policy(node):
    while not node.state.is_terminal():
        if not node.is_fully_expanded():
            return node.expand()
        else:
            node = node.best_child()
    return node

def default_policy(state):
    while not state.is_terminal():
        action = random.choice(state.available_actions())
        state, _ = state.next_state(action)
    return state.reward()

def backup(node, reward):
    while node is not None:
        node.visits += 1
        node.total_reward += reward
        node = node.parent
