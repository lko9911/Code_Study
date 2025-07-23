#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

const int NUM_STATES = 5;
const int NUM_ACTIONS = 2;
double Q[NUM_STATES][NUM_ACTIONS] = {0};

double alpha = 0.1;  // 학습률
double gamma = 0.9;  // 할인율
double epsilon = 0.1; // 탐험률

int choose_action(int state) {
    if ((rand() / double(RAND_MAX)) < epsilon)
        return rand() % NUM_ACTIONS;
    return Q[state][0] > Q[state][1] ? 0 : 1;
}

int get_next_state(int state, int action) {
    // 간단한 환경
    return (state + action) % NUM_STATES;
}

double get_reward(int state, int action) {
    return (state == NUM_STATES - 1) ? 1.0 : 0.0;
}

void train(int episodes) {
    for (int ep = 0; ep < episodes; ++ep) {
        int state = rand() % NUM_STATES;
        for (int t = 0; t < 100; ++t) {
            int action = choose_action(state);
            int next_state = get_next_state(state, action);
            double reward = get_reward(state, action);
            Q[state][action] += alpha * (reward + gamma * std::max(Q[next_state][0], Q[next_state][1]) - Q[state][action]);
            state = next_state;
        }
    }
}
