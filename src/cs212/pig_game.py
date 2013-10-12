'''
Created on Oct 12, 2013

@author: pglauner
'''

import random
from my_decorators import memo
from uncertainty import best_action

goal = 40
other = {1:0, 0:1}


def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me+1, 0) # pig out; other player's turn
    else:
        return (p, me, you, pending+d)  # accumulate die roll in pending


def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)


def dierolls():
    "Generate die rolls."
    while True:
        yield random.randint(1, 6)


def Q_pig(state, action, Pwin):  
    "The expected value of choosing action in state."
    if action == 'hold':
        return 1 - Pwin(hold(state))
    if action == 'roll':
        return (1 - Pwin(roll(state, 1))
                + sum(Pwin(roll(state, d)) for d in (2,3,4,5,6))) / 6.
    raise ValueError


def pig_actions(state):
    "The legal actions from a state."
    _, _, _, pending = state
    return ['roll', 'hold'] if pending else ['roll']


@memo        
def Pwin(state):
    """The utility of a state; here just the probability that an optimal player
    whose turn it is to move can win from the current state."""
    # Assumes opponent also plays with optimal strategy.
    (_, me, you, pending) = state
    if me + pending >= goal:
        return 1
    elif you >= goal:
        return 0
    else:
        return max(Q_pig(state, action, Pwin)
                   for action in pig_actions(state))


@memo
def win_diff(state):
    "The utility of a state: here the winning differential (pos or neg)."
    (_, me, you, pending) = state
    if me + pending >= goal or you >= goal:
        return (me + pending - you)
    else:
        return max(Q_pig(state, action, win_diff)
                   for action in pig_actions(state))


def max_diffs(state):
    """A strategy that maximizes the expected difference between my final score
    and my opponent's."""
    return best_action(state, pig_actions, Q_pig, win_diff)


def max_wins(state):
    "The optimal pig strategy chooses an action with the highest win probability."
    return best_action(state, pig_actions, Q_pig, Pwin)


def play_pig(A, B, dierolls=dierolls()):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    strategies = [A, B]
    state = (0, 0, 0, 0)
    while True:
        (p, me, you, _) = state
        if me >= goal:
            return strategies[p]
        elif you >= goal:
            return strategies[other[p]]
        else:
            action = strategies[p](state)
            if action == 'hold':
                state = hold(state)
            elif action == 'roll':
                state = roll(state, next(dierolls))
            # Illegal action
            else:
                return strategies[other[p]]

def test():
    winner = play_pig(max_wins, max_diffs) 
    return winner.__name__

if __name__ == '__main__':
    print test()
