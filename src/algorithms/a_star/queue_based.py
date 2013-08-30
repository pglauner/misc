'''
Created on Aug 28, 2013

@author: pglauner
'''
from collections import defaultdict
import heapq

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
    visited       = set()
    frontier_set  = set()
    frontier_heap = []
    path          = []
    came_from     = {}
    # Cost from start along best known path
    best_score = defaultdict(lambda: 0)

    heapq.heappush(frontier_heap, (0, start))
    frontier_set.add(start)
    while frontier_set:
        current = heapq.heappop(frontier_heap)[1]
        if current == end:
            return best_score[current], get_path(current, came_from)
        frontier_set.remove(current)
        visited.add(current)
        for neighbor in graph[current]:
            tentative_score = best_score[current] + graph[current][neighbor]
            if (neighbor not in visited and neighbor not in frontier_set) or tentative_score < best_score[neighbor]:
                came_from[neighbor] = current
                best_score[neighbor] = tentative_score
                heapq.heappush(frontier_heap, (tentative_score, neighbor))
                frontier_set.add(neighbor)

    return -1, path
