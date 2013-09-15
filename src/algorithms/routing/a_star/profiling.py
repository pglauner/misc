'''
Created on Aug 30, 2013

@author: pglauner
'''

import cProfile
import simple, queue_based
import algorithms.routing.test_graphs.test_graphs
import algorithms.routing.test_graphs.phrase_graphs


def find_route(impl):
    return impl.a_star(algorithms.routing.test_graphs.phrase_graphs.simple_phrase, 0, 1)


if __name__ == '__main__':
    cProfile.run('for i in range(100000): find_route(simple)')
    cProfile.run('for i in range(100000): find_route(queue_based)')
