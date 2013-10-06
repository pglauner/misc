'''
Created on Oct 6, 2013

@author: pglauner
'''
import itertools
from algorithms.routing.shortest_path import shortest_path_search


def more_pour_problem(capacities, goal, start=None):
    # your code here
    if not start:
        start = (0,) * len(capacities)
    return shortest_path_search(start, more_successors(capacities), lambda state: goal in state)


def more_successors(capacities):
    def replace(state, i, val):
        l = list(state)
        l[i] = val
        return tuple(l)

    def sc(state):
        res = {}
        indices = range(len(state))
        for i in indices:
            res[replace(state, i, capacities[i])] = ('fill', i)
            res[replace(state, i, 0)] = ('empty', i)
            for j in indices:
                if i != j:
                    x, y = state[i], state[j]
                    max_cap = capacities[j]
                    x, y = (0, y+x) if y+x <= max_cap else (x-(max_cap-y), (max_cap))
                    state2 = replace(state, i, x)
                    res[replace(state2, j, y)] = ('pour', i, j)
        return res
    return sc


if __name__ == '__main__':
    assert more_pour_problem((1, 2, 4, 8), 4) == [
        (0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
    assert more_pour_problem((1, 2, 4), 3) == [
        (0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)] 
    starbucks = (8, 12, 16, 20, 24)
    assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))
    assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))
    assert more_pour_problem((1, 3, 9, 27), 28) == []
