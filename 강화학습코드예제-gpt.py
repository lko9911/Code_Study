import gym
import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np
from collections import deque

# Q-Network 정의
class DQN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(DQN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim)
        )
    
    def forward(self, x):
        return self.fc(x)

# 환경 설정
env = gym.make('CartPole-v1')
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

# 하이퍼파라미터
lr = 0.001
gamma = 0.99
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01
batch_size = 64
memory = deque(maxlen=10000)
episodes = 100

# 네트워크와 옵티마이저
q_network = DQN(state_dim, action_dim)
optimizer = optim.Adam(q_network.parameters(), lr=lr)
loss_fn = nn.MSELoss()

# 경험을 이용한 학습 함수
def train():
    if len(memory) < batch_size:
        return
    batch = random.sample(memory, batch_size)
    states, actions, rewards, next_states, dones = zip(*batch)

    states = torch.FloatTensor(states)
    actions = torch.LongTensor(actions).unsqueeze(1)
    rewards = torch.FloatTensor(rewards)
    next_states = torch.FloatTensor(next_states)
    dones = torch.FloatTensor(dones)

    q_values = q_network(states).gather(1, actions).squeeze()
    next_q_values = q_network(next_states).max(1)[0]
    expected_q = rewards + gamma * next_q_values * (1 - dones)

    loss = loss_fn(q_values, expected_q.detach())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# 메인 루프
for episode in range(episodes):
    state, _ = env.reset()  # 최신 Gym은 (obs, info) 반환
    total_reward = 0
    done = False
    while not done:
        if random.random() < epsilon:
            action = env.action_space.sample()
        else:
            with torch.no_grad():
                action = q_network(torch.FloatTensor(state)).argmax().item()

        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

        memory.append((state, action, reward, next_state, float(done)))
        state = next_state
        total_reward += reward
        train()
    
    epsilon = max(epsilon_min, epsilon * epsilon_decay)
    print(f"Episode {episode + 1}, Reward: {total_reward}, Epsilon: {epsilon:.3f}")

env.close()
