'''
Created on Nov 9, 2013

@author: pglauner
'''
from algorithms.routing.shortest_path import shortest_path_search
from itertools import chain


tile_games = [#Solvable 
              (('E', 6, 5),
               (1, 3, 2),
               (7, 4, 0)),
              ((6, 5, 1),
               (3, 2, 7),
               (4, 0, 'E')),

              #Unsolvable
              ((6, 5, 1),
               (3, 2, 7),
               (0, 4, 'E')),

              #Solvable
              (('E', 1, 2, 3),
                (0, 4, 5, 6),
                (8, 9, 10, 7),
                (12, 13, 14, 11)),

              #Time-consuming
              #((10, 2, 5, 0),
              # (13, 'E', 4, 6),
              # (9, 3, 12, 1),
              # (14, 8, 11, 7)),
              ]


def get_y(pos, N):
    return pos / N


def successors(state):
    def generate_row_successors(state, transpose=False):
        """
        Generates row successors of a state.
        """
        original_state = state
        if transpose:
            state = tuple(zip(*state))

        N = len(state)
        y = get_y(list(chain(*state)).index('E'), N)
        row = list(state[y])
        row.remove('E')
        new_rows = [tuple(row[:i] + ['E'] + row[i:]) for i in xrange(N)]
        successors = {}
        for new_row in new_rows:
            new_state = list(state)
            new_state[y] = new_row
            new_state = tuple(new_state)
            if transpose:
                new_state = tuple(zip(*new_state))
            if new_state <> original_state:
                successors[new_state] = 'Col' if transpose else 'Row'
        return successors

    return dict(generate_row_successors(state).items()
                + generate_row_successors(state, True).items())


def is_goal(state):
    N = len(state)
    return tuple(chain(*state)) == tuple(range(N*N-1) + ['E'])


if __name__ == '__main__':
    for start in tile_games:
        print start
        shortest_path = shortest_path_search(start, successors, is_goal)
        print shortest_path
        print len(shortest_path) / 2, 'moves'
