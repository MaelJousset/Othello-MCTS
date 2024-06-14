# othello/othello_state.py
import gymnasium as gym

class OthelloState:
    def __init__(self, env, current_state=None, done=False, total_reward=0):
        self.env = env
        if current_state is None:
            self.current_state, _ = self.env.reset()
        else:
            self.current_state = current_state
        self.done = done
        self.total_reward = total_reward  # Initialize total_reward

    def available_actions(self):
        return list(range(self.env.action_space.n))

    def next_state(self, action):
        next_state, reward, done, _, _ = self.env.step(action)
        self.env.render()
        new_total_reward = self.total_reward + reward  # Accumulate the reward
        return OthelloState(self.env, current_state=next_state, done=done, total_reward=new_total_reward), action

    def is_terminal(self):
        return self.done

    def reward(self):
        return self.total_reward  # Return the accumulated reward
