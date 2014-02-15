'''
Created on Jan 29, 2014

@author: pglauner
'''

Fail = []

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                print state
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail


def shortest_path_search_new(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    # set of states we have visited, start visited initially
    explored = set([start])
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                print state
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail


goal = (0, 0, 0, 0, 1)

def is_goal(state):
    return state == goal

def successors(state):
    res = {}
    idx = state.index(1)
    change_idxs = [idx_new for idx_new in (idx - 1, idx + 1) if 0 <= idx_new < len(goal)]
    for change_idx in change_idxs:
        new_state = [0, 0, 0, 0, 0]
        new_state[change_idx] = 1
        res[tuple(new_state)] = 'to %s' % change_idx

    return res


if __name__ == '__main__':
    start = (1, 0, 0, 0, 0)
    path = shortest_path_search(start, successors, is_goal)
    print
    path = shortest_path_search_new(start, successors, is_goal)
