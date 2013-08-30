'''
Created on Aug 30, 2013

@author: pglauner
'''

import cProfile
import simple, queue_based
import test_graphs, phrase_graphs


def find_route(impl):
    return impl.a_star(phrase_graphs.simple_phrase, 0, 1)

cProfile.run('for i in range(100000): find_route(simple)')
cProfile.run('for i in range(100000): find_route(queue_based)')
