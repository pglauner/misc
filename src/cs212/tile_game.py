'''
Created on Nov 9, 2013

@author: pglauner
'''
from algorithms.routing.shortest_path import shortest_path_search


tile_games = [#Solvable 
              ((6, 5, 1),
               (3, 2, 7),
               (4, 0, 'E')),

              #Unsolvable
              ((6, 5, 1),
               (3, 2, 7),
               (0, 4, 'E')),

              #Time-consuming
#              (('E', 2, 3, 4),
#               (1, 5, 6, 7),
#               (9, 10, 11, 8),
#               (13, 14, 15, 12)),
              ]


def successors(N):
    def successors_n(state):
        res = {}
        e_x = 0
        e_y = 0
        # Find empty element
        for row_idx in range(len(state)):
            row = state[row_idx]
            if 'E' in row:
                e_y = row_idx
                e_x = row.index('E')
                break

        squashed_row = [v for v in row if v != 'E']
        for x in range(N):
            new_state = list(state)
            new_state[e_y] = tuple(squashed_row[:x] + ['E'] + squashed_row[x:])
            new_state = tuple(new_state)
            if new_state != state:
                res[new_state] = x

        squashed_col = [row[e_x] for row in state if row[e_x] != 'E']
        for y in range(N):
            new_state = list(state)
            new_col = tuple(squashed_col[:y] + ['E'] + squashed_col[y:])
            for y1 in range(N):
                new_state[y1] = list(new_state[y1])
                new_state[y1][e_x] = new_col[y1]
                new_state[y1] = tuple(new_state[y1])
            new_state = tuple(new_state)
            if new_state != state:
                res[new_state] = y

        return res

    return successors_n


def is_goal(N):
    def is_goal_n(state):
        l = range(N*N-1) + ['E']
        return tuple(zip(*[iter(l)]*N)) == state

    return is_goal_n


if __name__ == '__main__':
    for start in tile_games:
        N = len(start)
        shortest_path = shortest_path_search(start, successors(N), is_goal(N))
        print shortest_path
        print len(shortest_path) / 2
