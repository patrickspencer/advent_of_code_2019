"""
Day 3 Part 1
~~~~~~~~~~~~
"""

import os

fdir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(fdir, 'day3_input.txt')

with open(filename, 'r') as f:
    input = f.read().split('\n')
    
l1_commands = input[0].split(',')
l2_commands = input[1].split(',')

def pairwise_add(tuple1, tuple2):
    return tuple([sum(t) for t in zip(tuple1, tuple2)])

def make_points(commands):
    points = []
    last = [0,0]
    directions = {'U': (0,1),
                  'R': (1,0),
                  'L': (-1,0),
                  'D': (0,-1)}
    for command in commands:
        direction = directions[command[0]]
        steps = int(command[1:])
        for _ in range(steps):
            new = pairwise_add(last, direction)
            points.append(new)
            last = new
    return points

apoints = make_points(l1_commands)
bpoints = make_points(l2_commands)

intersection_points = list(set(apoints).intersection(set(bpoints)))

def manhattan_dist(point):
    return abs(point[0]) + abs(point[1])

closest_value = min(intersection_points, key=manhattan_dist)

print('closest point:', closest_value)
print('Distance from origin to closest point:', manhattan_dist(closest_value))