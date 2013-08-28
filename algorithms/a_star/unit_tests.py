'''
Created on Aug 28, 2013

@author: pglauner
'''

import unittest

from test_graphs import simple_graph, norvig_graph
from utils import get_unidirectional
import simple

class AStarTests(unittest.TestCase):
    def test_simple_graph(self):
        g = get_unidirectional(simple_graph)
        self.assertEqual(simple.a_star(g, 0, 0), (0, [0]))
        self.assertEqual(simple.a_star(g, 0, 2), (1, [0, 2]))
        self.assertEqual(simple.a_star(g, 0, 4), (3, [0, 2, 4]))

        simple_graph[1][4] = 1.4
        g = get_unidirectional(simple_graph)
        self.assertEqual(simple.a_star(g, 0, 4), (2.9, [0, 1, 4]))

    def test_norvig_graph(self):
        g = get_unidirectional(norvig_graph)
        self.assertEqual(simple.a_star(g, 'A', 'A'), (0, ['A']))
        self.assertEqual(simple.a_star(g, 'A', 'B'), (418, ['A', 'S', 'R', 'P', 'B']))
        self.assertEqual(simple.a_star(g, 'B', 'A'), (418, ['B', 'P', 'R', 'S', 'A']))
        self.assertEqual(simple.a_star(g, 'A', 'C'), (366, ['A', 'S', 'R', 'C']))
        self.assertEqual(simple.a_star(g, 'A', 'D'), (374, ['A', 'T', 'L', 'M', 'D']))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AStarTests)
    unittest.TextTestRunner(verbosity=2).run(suite)