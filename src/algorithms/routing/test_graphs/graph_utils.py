'''
Created on Sep 15, 2013

@author: pglauner
'''

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
