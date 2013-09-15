'''
Created on Aug 28, 2013

@author: pglauner
'''
from collections import defaultdict

def get_path(node, came_from):
    path = []
    while node is not None:
        path.append(node)
        node = came_from.get(node, None)
    path.reverse()
    return path


def a_star(graph, start, end):
    """
    No heuristic function, simple shortest path algorithm.
    """
    visited   = set()
    frontier  = set()
    path      = []
    came_from = {}
    # Cost from start along best known path
    best_score = defaultdict(lambda: 0)

    frontier.add(start)
    best_score[start] = 0
    while frontier:
        current = min(frontier, key=lambda c: best_score[c])
        if current == end:
            return best_score[current], get_path(current, came_from)
        frontier.remove(current)
        visited.add(current)
        for neighbor in graph[current]:
            tentative_score = best_score[current] + graph[current][neighbor]
            if (neighbor not in visited and neighbor not in frontier) or tentative_score < best_score[neighbor]:
                came_from[neighbor] = current
                best_score[neighbor] = tentative_score
                frontier.add(neighbor)

    return -1, path
