'''
Created on Aug 28, 2013

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


def get_phrase(path):
    return ' '.join(path[1:-1])


def get_edge_count(graph):
    count = 0
    for values in graph.values():
        count += len(values)
    return count
