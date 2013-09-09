'''
Created on Sep 8, 2013

@author: pglauner
'''

def pour_problem(X, Y, goal, start = (0, 0)):
    if goal == start:
        return [start]
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        (x, y) = path[-1]
        for (state, action) in successors(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if state == goal:
                    return path2
                else:
                    frontier.append(path2)
    return []


def successors(x, y, X, Y):
    assert x <= X and y <= Y
    return {((0, y+x) if y+x <= Y else (x-(Y-y), (Y))): 'x->y',
            ((x+y, 0) if x+y <= X else (X, (y-(X-x)))): 'x<-y',
            (X, y): 'fill x',
            (x, Y): 'fill y',
            (0, y): 'empty x',
            (x, 0): 'empty y'}


if __name__ == '__main__':
    res = pour_problem(418, 986, (6, 0), (0, 0))
    print res
    print '%s transitions' % (len(res) / 2)
