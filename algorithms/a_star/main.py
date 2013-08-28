'''
Created on Aug 28, 2013

@author: pglauner
'''

from test_graph import graph
import utils
import first_attempt


uni_graph = utils.get_unidirectional(graph)

print first_attempt.a_star(uni_graph, 'A', 'B')
print first_attempt.a_star(uni_graph, 'B', 'A')
