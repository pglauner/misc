'''
Created on Nov 11, 2013

@author: pglauner
'''

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

N_y = len(colors)
N_x = len(colors[0])


p = [[1./(N_x * N_y)]*N_x for _ in range(N_y)]


def move(p, m):
    m_y, m_x = m
    q_temp = []
    q = [[0]*N_x for _ in range(N_y)]
    if abs(m_y) == 1:
        q_temp = [p[(y - m_y)] for y in range(N_y)]
    elif abs(m_x) == 1:
        q_temp = [row[-m_x:] + row[:-m_x] for row in p]
    else:
        return p
    #Considers probabilistic moving
    for y in range(N_y):
        for x in range(N_x):
            q[y][x] = p_move * q_temp[y][x] + (1 - p_move) * p[y][x]
    return q


def sense(p, m):
    q = [[0]*N_x for _ in range(N_y)]
    s = 0
    for y in range(N_y):
        for x in range(N_x):
            hit = (colors[y][x] == m)
            q[y][x] = p[y][x] * ((hit * sensor_right) + (1-hit) * (1 - sensor_right))
            s += q[y][x]
    # Normalizes probabilities
    for y in range(N_y):
        for x in range(N_x):
            q[y][x] /= s
    return q


if __name__ == '__main__':
    for i in range(len(measurements)):
        p = move(p, motions[i])
        p = sense(p, measurements[i])

    #Your probability array must be printed 
    #with the following code.

    show(p)
