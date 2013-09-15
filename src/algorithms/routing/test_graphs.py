'''
Created on Aunorvig_graph 28, 2013

@author: pnorvig_graphlauner
'''

# See Artificial Intelligence A Modern Approach, Third Edition Finorvig_graphure 3.2

norvig_graph = {}
norvig_graph['A'] = {'S': 140, 'T': 118, 'Z': 75}
norvig_graph['Z'] = {'O': 71}
norvig_graph['O'] = {'S': 151}
norvig_graph['T'] = {'L': 111}
norvig_graph['L'] = {'M': 70}
norvig_graph['M'] = {'D': 75}
norvig_graph['D'] = {'C': 120}
norvig_graph['S'] = {'F': 99, 'R': 80}
norvig_graph['F'] = {'B': 211}
norvig_graph['R'] = {'C': 146, 'P': 97}
norvig_graph['C'] = {'P': 138}
norvig_graph['P'] = {'B': 101}
norvig_graph['B'] = {'G': 90, 'U': 85}
norvig_graph['U'] = {'V': 142, 'H': 98}
norvig_graph['V'] = {'I': 92}
norvig_graph['I'] = {'N': 87}
norvig_graph['H'] = {'E': 86}

simple_graph = {}
simple_graph[0] = {1: 1.5, 2: 1, 3: 1.2}
simple_graph[2] = {4: 2}
simple_graph[3] = {4: 2}
simple_graph[1] = {4: 1.5}