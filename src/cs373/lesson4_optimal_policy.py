'''
Created on Nov 25, 2013

@author: pglauner
'''

from heapq import heappush, heappop

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.


def get_inverse_action(idx):
    num_actions = len(delta)
    return (idx + num_actions/2) % num_actions

def successors(y, x):
    res = []
    for action_idx, d in enumerate(delta):
        dy, dx = d
        next_y = y + dy
        next_x = x + dx
        if 0 <= next_y < len(grid) and 0 <= next_x < len(grid[0]):
            res.append((next_y, next_x, action_idx))
    return res

def optimum_policy():
    policy = [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    frontier = []
    heappush(frontier, (0, goal[0], goal[1], 0))
    explored = set([(goal[0], goal[1])])
    while frontier:
        val, y, x, action_idx = heappop(frontier)
        # Ceil values of non-reachable cells
        norm_val = min(val, 99)
        if norm_val < 99:
            policy[y][x] = delta_name[get_inverse_action(action_idx)]
        for next_y, next_x, action_idx in successors(y, x):
            if (next_y, next_x) not in explored:
                explored.add((next_y, next_x))
                if grid[next_y][next_x] == 1:
                    next_val = 99
                else:
                    next_val = val + 1
                heappush(frontier, (next_val, next_y, next_x, action_idx))
    policy[goal[0]][goal[1]] = '*'
    return policy

if __name__ == '__main__':
    vals = optimum_policy()
    for row in vals:
        print row
