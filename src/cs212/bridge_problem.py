'''
Created on Sep 15, 2013

@author: pglauner
'''

from algorithms.routing.shortest_path import shortest_path_search
from algorithms.routing.lowest_cost import lowest_cost_search


def successors(state):
    _, _, light = state
    return dict(successor(state, frozenset([a, b]))
                for a in state[light]
                for b in state[light])


def successor(state, travellers):
    _, _, light = state
    start = state[light] - travellers
    dest = state[1-light] | travellers
    if light == 0:
        return (start, dest, 1), (travellers, '->')
    else:
        return (dest, start, 0), (travellers, '<-')


def is_goal(state):
    here, _, _ = state
    return len(here) == 0


if __name__ == '__main__':
    # light: left=0, right=1
    start = here, there, light = frozenset([1, 2, 5, 10]), frozenset([]), 0

    print shortest_path_search(start, successors, is_goal)
    print lowest_cost_search(start, successors, is_goal, lambda action: max(action[0]))
