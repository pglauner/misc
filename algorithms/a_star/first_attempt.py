'''
Created on Aug 28, 2013

@author: pglauner
'''


def a_star(graph, start, end):
    """
    No heuristic function, simple shortest path algorithm.
    """
    visited   = set()
    frontier  = set()
    path      = []
    came_from = {}
    # Cost from start along best known path
    best_score = {}

    def get_path(node):
        next_node = node
        while next:
            path.append(next_node)
            if next_node in came_from:
                next_node = came_from[next_node]
            else:
                break
        path.reverse()
        return path

    frontier.add(start)
    best_score[start] = 0
    while frontier:
        current  = min(frontier, key=lambda x: best_score[x])
        if current == end:
            return best_score[current], get_path(current)
        frontier.remove(current)
        visited.add(current)
        for neighbor in graph[current]:
            tentative_score = best_score[current] + graph[current][neighbor]
            if neighbor not in visited:
                if neighbor not in frontier or tentative_score < best_score[neighbor]:
                    came_from[neighbor] = current
                    best_score[neighbor] = tentative_score
                    frontier.add(neighbor)

    return -1, path
