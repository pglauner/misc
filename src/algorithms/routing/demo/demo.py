'''
Created on Sep 15, 2013

@author: pglauner
'''

from algorithms.routing.shortest_path import shortest_path_search
from algorithms.routing.lowest_cost import lowest_cost_search
from algorithms.routing.a_star.simple import a_star as a_star_simple
from algorithms.routing.a_star.queue_based import a_star as a_star_queue
from algorithms.routing.test_graphs.test_graphs import tricky_graph
from algorithms.routing.test_graphs.phrase_graphs import simple_phrase
from algorithms.routing.test_graphs.graph_utils import action_cost, is_goal, successors


if __name__ == '__main__':
    print shortest_path_search(0, successors(tricky_graph), is_goal(100))
    print lowest_cost_search(0, successors(tricky_graph), is_goal(100), action_cost)
    print a_star_simple(tricky_graph, 0, 100)
    print a_star_queue(tricky_graph, 0, 100)

    print

    print shortest_path_search(0, successors(simple_phrase), is_goal(1))
    print lowest_cost_search(0, successors(simple_phrase), is_goal(1), action_cost)
    print a_star_simple(simple_phrase, 0, 1)
    print a_star_queue(simple_phrase, 0, 1)
