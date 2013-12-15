'''
Created on Nov 30, 2013

@author: pglauner
'''
from math import *
import copy

path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]


def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance=0.0000001):
    newpath = copy.deepcopy(path)

    change = 1.0
    while change > tolerance:
        change = 0.0
        for i in range(1, len(path) - 1):
            for j in range(len(path[0])):
                aux = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j])
                newpath[i][j] += weight_smooth * (newpath[i+1][j] + newpath[i-1][j] - 2*newpath[i][j])               
                change += abs(aux - newpath[i][j])

    return newpath

if __name__ == '__main__':
    newpath = smooth(path)
    for i in range(len(path)):
        print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'
