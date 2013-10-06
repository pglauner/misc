'''
Created on Oct 6, 2013

@author: pglauner
'''

from collections import defaultdict

def subway(**lines):
    """Define a subway map. Input is subway(linename='station1 station2...'...).
    Convert that and return a dict of the form: {station:{neighbor:line,...},...}"""
    def get_neighboring_stations(stations):
        return [stations[i:i+2] for i in xrange(len(stations) - 1)]

    res = defaultdict(dict)
    for line, stations in lines.iteritems():
        for a, b in get_neighboring_stations(stations.split()):
            res[a][b] = line
            res[b][a] = line
    return res


boston = subway(
    blue='bowdoin government state aquarium maverick airport suffolk revere wonderland',
    orange='oakgrove sullivan haymarket state downtown chinatown tufts backbay foresthills',
    green='lechmere science north haymarket government park copley kenmore newton riverside',
    red='alewife davis porter harvard central mit charles park downtown south umass mattapan')


def ride(here, there, system=boston):
    "Return a path on the subway system from here to there."
    ## your code here
    return shortest_path_search(here, lambda s: system[s], lambda s: s == there)


def longest_ride(system):
    """"Return the longest possible 'shortest path' 
    ride between any two stops in the system."""
    stops = set([s for dic in system.values() for s in dic])
    return max([ride(a, b, system) for a in stops for b in stops], key=len)


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
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []


def path_states(path):
    "Return a list of states in this path."
    return path[0::2]


def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]


if __name__ == '__main__':
    assert ride('mit', 'government') == [
        'mit', 'red', 'charles', 'red', 'park', 'green', 'government']
    assert ride('mattapan', 'foresthills') == [
        'mattapan', 'red', 'umass', 'red', 'south', 'red', 'downtown',
        'orange', 'chinatown', 'orange', 'tufts', 'orange', 'backbay', 'orange', 'foresthills']
    assert ride('newton', 'alewife') == [
        'newton', 'green', 'kenmore', 'green', 'copley', 'green', 'park', 'red', 'charles', 'red',
        'mit', 'red', 'central', 'red', 'harvard', 'red', 'porter', 'red', 'davis', 'red', 'alewife']
    assert (path_states(longest_ride(boston)) == [
        'wonderland', 'revere', 'suffolk', 'airport', 'maverick', 'aquarium', 'state', 'downtown', 'park',
        'charles', 'mit', 'central', 'harvard', 'porter', 'davis', 'alewife'] or 
        path_states(longest_ride(boston)) == [
                'alewife', 'davis', 'porter', 'harvard', 'central', 'mit', 'charles', 
                'park', 'downtown', 'state', 'aquarium', 'maverick', 'airport', 'suffolk', 'revere', 'wonderland'])
    assert len(path_states(longest_ride(boston))) == 16
