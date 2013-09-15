'''
Created on Sep 8, 2013

@author: pglauner
'''

from algorithms.routing.shortest_path import shortest_path_search
from algorithms.routing.lowest_cost import lowest_cost_search


def successors(X, Y):
    def sc(state):
        x, y = state
        assert x <= X and y <= Y
        return {((0, y+x) if y+x <= Y else (x-(Y-y), (Y))): 'x->y',
                ((x+y, 0) if x+y <= X else (X, (y-(X-x)))): 'x<-y',
                (X, y): 'fill x',
                (x, Y): 'fill y',
                (0, y): 'empty x',
                (x, 0): 'empty y'}
    return sc


if __name__ == '__main__':
    res = shortest_path_search((0, 0), successors(418, 986), lambda state: state == (6, 0))
    print res
    print '%s transitions' % (len(res) / 2)
    print
    res = lowest_cost_search((0, 0), successors(418, 986), lambda state: state == (6, 0), lambda action: 1)
    print res
    print '%s transitions' % (len(res) / 2)
