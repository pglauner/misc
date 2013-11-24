'''
Created on Nov 24, 2013

@author: pglauner
'''

grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
            [8, 7, 6, 5, 4, 3],
            [7, 6, 5, 4, 3, 2],
            [6, 5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1, 0]]

# Empty heuristic results in naive first-search
#heuristic = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1


def h_grid(x, y):
    return heuristic[x][y]

# Copied from Udacity, see better implementations in /src/algorithms
def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]


    x = init[0]
    y = init[1]
    g = 0
    h = h_grid(x, y)
    f = g + h

    frontier = [[f, g, h, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    count = 0
    
    while not found and not resign:
        if len(frontier) == 0:
            resign = True
            return "Fail"
        else:
            frontier.sort()#key=lambda s: s[1])
            frontier.reverse()
            next_state = frontier.pop()
            x = next_state[3]
            y = next_state[4]
            g = next_state[1]
            expand[x][y] = count
            count += 1
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = h_grid(x2, y2)
                            f2 = g2 + h2
                            frontier.append([f2, g2, h2, x2, y2])
                            closed[x2][y2] = 1
    for i in range(len(expand)):
        print expand[i]
    return expand

if __name__ == '__main__':
    search()
