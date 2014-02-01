'''
Created on Jan 30, 2014

@author: pglauner

Initial implementation of value iteration to solve finite-state Markov Decision Processes (MDPs).
Could undergo some improvements to create better policies for cases shown in the book.


Amended world from Artificial Intelligence: A Modern Approach, Chapter 17:
-------------
|  |  |  |+1|
|  |--|-1|-1|
|  |  |  |  |
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
directions = {0: '^',
              1: '>',
              2: 'v',
              3: '<'}

rewards = {6: -1,
           9: -1,
           10: 1,
           'else': -0.04
           }

def print_world(world, show_directions=False):
    if show_directions:
        world = [directions[idx] for idx in world]
    # Adds blocked cell
    full_world = world[:4] + ['-'] + world[4:]
    # Converts line into printable matrix format
    for line in reversed(zip(*zip(*[iter(full_world)]*3))):
        print ' '.join(['%s' % element for element in line])


def R(s):
    """
    Reward function
    """
    return rewards.get(s, rewards['else'])


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
    for action in (a_idx - 1, a_idx, (a_idx + 1) % 4):
        dx, dy = actions[action]
        nx, ny = x + dx, y + dy
        new_s = get_id((nx, ny))

        # Only goes to valid destinations, remains in state otherwise
        destination = new_s
        if new_s < 0:
            destination = s

        # Higher probability for intended direction
        p = 0.1
        if action == a_idx:
            p = 0.8
        res[destination] = p

    return res


def value_iteration(epsilon=10e-5, gamma=0.99):
    V = [0] * len(states)
    delta = 1
    for s, val in rewards.iteritems():
        if type(s) == int:
            V[s] = val
    while abs(delta) > epsilon:
        delta = 0
        for s, val in enumerate(V):
            if s not in rewards:
                future_rewards = (sum(p * V[s1] for s1, p in P(s, a).iteritems()) for a in actions)
                new_val = R(s) + gamma * max(future_rewards)
                delta += abs(new_val - val)
                V[s] = new_val
    return V


def get_optimal_policy(v_star):
    pi = [''] * len(states)
    for s in range(len(pi)):
        values = [sum(p * v_star[n1] for n1, p in P(s, a).iteritems()) for a in actions]
        pi[s] = values.index(max(values))
    return pi

v_star = value_iteration()
policy = get_optimal_policy(v_star)
print_world(v_star)
print_world(policy, True)
