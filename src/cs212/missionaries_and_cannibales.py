'''
Created on Sep 15, 2013

@author: pglauner
'''

from algorithms.routing.shortest_path import shortest_path_search
from algorithms.routing.lowest_cost import lowest_cost_search
import itertools


combs = [c for c in itertools.combinations_with_replacement('MC ', 2) if c != (' ', ' ')]


def successors(state):
    M1, C1, B1, M2, C2, B2 = state
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}
    res = {}
    for x, y in combs:
        action = ''
        if B1:
            m1, c1, b1, m2, c2, b2 = M1, C1, 0, M2, C2, 1
        elif B2:
            m1, c1, b1, m2, c2, b2 = M2, C2, 1, M1, C1, 0
        for z in (x, y):
            if z == 'M':
                m1 -= 1
                m2 += 1
                action += 'M'
            if z == 'C':
                c1 -= 1
                c2 += 1
                action += 'C'
        if all(x >= 0 for x in (m1, c1, b1, m2, c2, b2)):
            if B1:
                res[(m1, c1, b1, m2, c2, b2)] = action + '->'
            elif B2:
                res[(m2, c2, b1, m1, c1, b2)] = '<-' + action

    return res


def is_goal(start):
    def g(state):
        return state == (0, 0, 0) + start
    return g


if __name__ == '__main__':
    start = m1, c1, b1, m2, c2, b2 = 3, 3, 1, 0, 0, 0

    print shortest_path_search(start, successors, is_goal(start[0:3]))
    print lowest_cost_search(start, successors, is_goal(start[0:3]), lambda action: 1)
