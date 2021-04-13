import numpy as np
import pandas as pd
from numba_functions import simulate_observations

class SimulateData:

    def __init__(self):
        pass

    def simulate_data(self, state_transition=None, emission_prob=None, initial_state=None, num_obs=100, continuous=True):

        if continuous:
            return self.simulate_continuous(state_transition, emission_prob, initial_state, num_obs)

        else:
            return self.simulate_discrete()


    def simulate_continuous(self, state_transition, emission_prob, initial_state, num_obs):
        if state_transition is None:
            state_transition = np.array([[0.8, 0.1, 0.1],
                                         [0.05, 0.85, 0.1],
                                         [0.05, 0.05, 0.9]])

        if emission_prob is None:
            emission_prob = np.array([[0, 0.5],
                                      [1, 0.5],
                                      [2, 0.5]])

        if initial_state is None:
            initial_state = np.array([1/3, 1/3, 1/3])

        observations = simulate_observations(num_obs, initial_state, emission_prob, state_transition)

        # observations = np.zeros(num_obs)
        # state_path = np.zeros(num_obs)
        # curr_state = np.argmax(np.random.multinomial(1, initial_state, 1))
        #
        # for i in range(num_obs):
        #     state_path[i] = curr_state
        #     observations[i] = np.random.normal(emission_prob[curr_state, 0], emission_prob[curr_state, 1])
        #     curr_state = np.argmax(np.random.multinomial(1, state_transition[curr_state, :]))

        # generate random initialization
        A = self.generate_random_state_transition_matrix(state_transition.shape[0], state_transition.shape[1])
        B = self.generate_random_emission_matrix(emission_prob.shape[0], emission_prob.shape[1])
        state_path_sim = self.generate_random_state_path(A.shape[0], num_obs)

        initial = np.zeros(state_transition.shape[0])
        initial[0] = 1  # begin at the first state

        return observations, state_path_sim, A, B, initial

    def simulate_discrete(self):

        # load data and create HMM object
        obs = pd.read_csv('../data/dummy_data.csv')['Visible'].values + 1

        pi = np.array([.5, .5])  # initial dist.
        # Transition Probabilities   {A,B} are the states
        # A = [[p(A|A), p(B|A)],
        #      [p(A|B), p(B|B)]]
        A = np.ones((2, 2))
        A = A / np.sum(A, axis=1)

        # Emission Probabilities    {1,2,3} are the emissions
        # B = [[p(1|A), p(2|A), p(3|A)],
        #      [p(1|B), p(2|B), p(3|B)]]
        B = np.array(((1, 3, 5), (2, 4, 6)))
        B = B / np.sum(B, axis=1).reshape((-1, 1))

        return obs, A, B, pi

    def generate_random_state_transition_matrix(self, nrow, ncol):
        x = np.random.random((nrow, ncol))

        rsum = None
        csum = None

        while (np.any(rsum != 1)) | (np.any(csum != 1)):
            x /= x.sum(0)
            x = x / x.sum(1)[:, np.newaxis]
            rsum = x.sum(1)
            csum = x.sum(0)

        return x

    def generate_random_emission_matrix(self, nrow, ncol):
        initial = np.random.normal(1, 0.5)
        emission_matrix = np.zeros((nrow, ncol))
        for row in range(nrow):
            emission_matrix[row, :] = [initial*(row+1), 0.5]

        return emission_matrix


    def generate_random_state_path(self, num_states, num_obs):
        return np.random.choice(np.arange(num_states), num_obs)

#######

A = np.array([[0.6, 0.3, 0.1], [0.1,0.8,0.1],[0.1,0.3,0.6]])
mu = np.array([-2, 0, 2])


def marginal(A, init):
    return np.dot(A.T, init)

def generate_num():
    return random.uniform(0, 1)

def generate_state(v, num):
    n = len(v)
    for i in range(3):
        if num < sum(v[:i+1]):
            a = i
            return a

def generate_obs(state):
    if state == 0:
        a = np.random.normal(-2, 1)
    elif state == 1:
        a = np.random.normal(0, 1)
    else:
        a = np.random.normal(2, 1)
    return a

converge = False
init = np.array([1/3,1/3,1/3])
while not converge:
    update = marginal(A, init)
    if ((update != init).all()):
        init = update
    else:
        converge = True
init = np.array([0.2,0.6,0.2])

state = np.zeros(1000)
obs = np.zeros(1000)
state[0] = generate_state(init, generate_num())
obs[0] = generate_obs(state[0])

for i in np.arange(1, 1000):
    tran = A[int(state[i-1])]
    state[i] = generate_state(tran, generate_num())
    obs[i] = generate_obs(state[i])

# plt.figure()
# plt.plot(obs)
# fname = os.path.join("/Users/xiaoxuanliang/Desktop/STAT 520A/STAT-520A-Project", "plots", "original")
# plt.savefig(fname)
# print("\nFigure saved as '%s'" % fname)
# plt.plot(state)
# plt.show()