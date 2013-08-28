'''
Created on Aug 28, 2013

@author: pglauner
'''

from test_graphs import norvig_graph
import utils
import first_attempt


uni_graph = utils.get_unidirectional(norvig_graph)

print first_attempt.a_star(uni_graph, 'A', 'B')
print first_attempt.a_star(uni_graph, 'B', 'A')
