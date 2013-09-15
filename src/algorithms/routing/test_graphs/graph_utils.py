'''
Created on Sep 15, 2013

@author: pglauner
'''

from collections import defaultdict


def get_unidirectional(graph):
    res = defaultdict(lambda: defaultdict(dict))
    for from_node in graph:
        for to_node in graph[from_node]:
            distance = graph[from_node][to_node]
            res[from_node][to_node] = distance
            res[to_node][from_node] = distance
    return res


def successors(graph):
    def sc(state):
        if state not in graph:
            return {}
        return dict((s,
                    (state, s, graph[state][s]))
                    for s in graph[state].keys())
    return sc


def is_goal(goal):
    return lambda state: state == goal


def action_cost(action):
    return action[2]
