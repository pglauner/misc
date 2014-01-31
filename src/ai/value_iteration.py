'''
Created on Jan 30, 2014

@author: pglauner

Implements value iteration to solve finite-state Markov Decision Processes (MDPs).


Slightly changed world from Artificial Intelligence: A Modern Approach, Chapter 17:
-------------
|   |   |   | +1|
|   |---|   | -1|
|   |   |   |  |
-------------

State IDs:
-------------
| 2| 4| 7|10|
| 1|--| 6| 9|
| 0| 3| 5| 8|
-------------

States coordinates:
-------------------------
|(1,3)|(2,3)|(3,3)|(4,3)|
|(1,2)|-----|(3,2)|(4,2)|
|(1,1)|(2,1)|(3,1)|(4,1)|
-------------------------

'''

from test.test_decorators import memoize

# Generates all valid states
states = {0: (1, 1),
          1: (1, 2),
          2: (1, 3),
          3: (2, 1),
          4: (2, 3),
          5: (3, 1),
          6: (3, 2),
          7: (3, 3),
          8: (4, 1),
          9: (4, 2),
          10: (4, 3),
          }

# Nort, south, east west
actions = ((0, 1), (1, 0), (0, -1), (-1, 0))



def R(s):
    """
    Reward function
    """
    if s == 10:
        return 1
    elif s == 9:
        return -1
    else:
        return -0.04


@memoize
def P(s, a):
    """
    Transition probabilities function
    """
    def get_id(state):
        for s, coord in states.iteritems():
            if coord == state:
                return s
        return -1

    res = dict()
    x, y = states[s]
    a_idx = actions.index(a)

    # Action and moves at right angles
    for dx, dy in [actions[i] for i in (a_idx - 1, a_idx, (a_idx + 1) % 4)]:
        nx, ny = x + dx, y + dy
        new_s = get_id((nx, ny))
        # State must be valid
        if new_s >= 0:
            p = 0.1
            if (dx, dy) == a:
                p = 0.8
            res[new_s] = p

    return res


def value_iteration(epsilon = 10e-5, gamma=0.95):
    V = [0] * len(states)
    delta = 1
    i = 0
    while abs(delta) > epsilon / gamma:
        i += 1
        delta = 0
        for s, val in enumerate(V):
            future_rewards = (sum(p * V[n_s] for n_s, p in P(s, a).iteritems()) for a in actions)
            new_val = R(s) + gamma * max(future_rewards)
            delta += abs(new_val - val)
            V[s] = new_val
    print i
    return V


def get_optimal_policy():
    V_star = value_iteration()
    print V_star
    PI = [''] * len(states)
    for s in range(len(PI)):
        values = [sum(p * V_star[n_s] for n_s, p in P(s, a).iteritems()) for a in actions]
        PI[s] = values.index(max(values))
    return PI

print get_optimal_policy()
