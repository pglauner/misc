'''
Created on Aug 28, 2013

@author: pglauner
'''

import unittest
import nose
import copy

from test_graphs import simple_graph, norvig_graph
from phrase_graphs import simple_phrase
from utils import get_unidirectional, get_phrase
import simple
import queue_based


IMPLEMENTATIONS = (simple, queue_based)


class AStarSimpleGraphTests(unittest.TestCase):

    def setUp(self):
        self._basic_graph = copy.deepcopy(simple_graph)
        self.g = get_unidirectional(self._basic_graph)

    def test_simple_graph1(self):
        for impl in IMPLEMENTATIONS:
            self.assertEqual(impl.a_star(self.g, 0, 0), (0, [0]))
            self.assertEqual(impl.a_star(self.g, 0, 2), (1, [0, 2]))
            self.assertEqual(impl.a_star(self.g, 0, 4), (3, [0, 2, 4]))
            self.assertEqual(impl.a_star(self.g, 4, 0), (3, [4, 1, 0]))

            self._basic_graph[1][4] = 1.4
            g = get_unidirectional(self._basic_graph)
            self.assertEqual(impl.a_star(g, 0, 4), (2.9, [0, 1, 4]))


class AStarNorvigGraphTests(unittest.TestCase):

    def setUp(self):
        self._basic_graph = norvig_graph
        self.g = get_unidirectional(self._basic_graph)

    def test_norvig_graph(self):
        for impl in IMPLEMENTATIONS:
            self.assertEqual(impl.a_star(self.g, 'A', 'A'), (0, ['A']))
            self.assertEqual(impl.a_star(self.g, 'A', 'B'), (418, ['A', 'S', 'R', 'P', 'B']))
            self.assertEqual(impl.a_star(self.g, 'B', 'A'), (418, ['B', 'P', 'R', 'S', 'A']))
            self.assertEqual(impl.a_star(self.g, 'A', 'C'), (366, ['A', 'S', 'R', 'C']))
            self.assertEqual(impl.a_star(self.g, 'A', 'D'), (374, ['A', 'T', 'L', 'M', 'D']))


class AStarSimplePhraseTests(unittest.TestCase):

    def test_norvig_graph(self):
        p = simple_phrase
        for impl in IMPLEMENTATIONS:
            dist, phrase = impl.a_star(p, 0, 1)
            self.assertEqual((dist, get_phrase(phrase)), (0.7, 'This was a great test'))


if __name__ == '__main__':
    nose.main()
