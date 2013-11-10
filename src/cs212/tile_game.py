'''
Created on Nov 9, 2013

@author: pglauner
'''
from algorithms.routing.shortest_path import shortest_path_search


tile_games = [#Solvable 
              ('E', 6, 5, 1, 3, 2, 7, 4, 0),
              (6, 5, 1, 3, 2, 7, 4, 0, 'E'),

              #Unsolvable
              (6, 5, 1, 3, 2, 7, 0, 4, 'E'),

              #Solvable
              ('E', 1, 2, 3, 0, 4, 5, 6, 8, 9, 10, 7, 12, 13, 14, 11),

              #Time-consuming
              #(10, 2, 5, 0, 13, 'E', 4, 6, 9, 3, 12, 1, 14, 8, 11, 7),
              ]


tile_lens = {1:1, 4:2, 9:3, 16:4}


def get_y_x(pos, N):
    y = pos / N
    x = pos % N
    return y, x


def successors(N):
    def move_row_or_col(state, res, idx1, idx2, action, offset=1):
        squashed_values = [v for v in state[idx1:idx2:offset] if v != 'E']
        for i in range(N):
            new_state = list(state)
            new_state[idx1:idx2:offset] = tuple(squashed_values[:i] + ['E'] + squashed_values[i:])
            new_state = tuple(new_state)
            if new_state != state:
                res[new_state] = action

    def successors_n(state):
        res = {}
        empty_y, empty_x = get_y_x(state.index('E'), N)

        row_idx1 = empty_y * N
        row_idx2 = row_idx1 + N
        move_row_or_col(state, res, row_idx1, row_idx2, 'Row')

        col_idx1 = empty_x
        col_idx2 = N * (N - 1) + empty_x % N + 1
        move_row_or_col(state, res, col_idx1, col_idx2, 'Col', N)

        return res

    return successors_n


def is_goal(N):
    def is_goal_n(state):
        return tuple(range(N*N-1) + ['E']) == state

    return is_goal_n


if __name__ == '__main__':
    for start in tile_games:
        N = tile_lens[len(start)]
        print start
        shortest_path = shortest_path_search(start, successors(N), is_goal(N))
        print shortest_path
        print len(shortest_path) / 2, 'moves'
