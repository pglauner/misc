'''
Created on Jan 30, 2014

@author: pglauner

Implements value iteration to solve finite-state Markov Decision Processes (MDPs).


Sample world:
-------------
|  |  |  |+1|
|  |--|  |-1|
|  |  |  | |
-------------

State IDs:
-------------
|(1,3)|(2,3)|(3,3)|(4,3)|
|(1,2)|-----|(3,2)|(4,2)|
|(1,1)|(2,1)|(3,1)|(4,1)|
-------------

'''

def reward(state):
    if state == (4, 3):
        return 1
    elif state == (4, 2):
        return -1
    else:
        return -0.02

def value_iteration(n, r, p, epsilon = 10e-5):
    v = list(range(n))
    delta = 0
    while abs(delta) > epsilon:
        pass
    return v
