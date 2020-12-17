import numpy as np
from itertools import product
from data import inputGen

f = inputGen.getPuzzle(2020, 17)
file = f.input_data
file = file.split()

active_points = set()

for y, row in enumerate(file):
    for x, col in enumerate(row):
        if col == '#':
            active_points.add((x,y,0))

comb = product([-1,0,1], repeat=3)
dirs = list(comb)
dirs.remove((0,0,0))

def get_neighbors(point, dirs):
    new_points = set()
    for d in dirs:
        new_points.add(tuple(np.array(d) + np.array(point)))
    return new_points

def change_to_active(point, active_points):
    global dirs
    neighbors = get_neighbors(point, dirs)
    if len(neighbors.intersection(active_points)) == 3:
        return True
    else:
        return False

def change_to_inactive(point, active_points):
    global dirs
    neighbors = get_neighbors(point, dirs)
    if len(neighbors.intersection(active_points)) in [2, 3]:
        return False
    else:
        return True

for cycle in range(6):
    neighbors = set()
    next_cycle_active = set()
    for point in active_points:
        neighbors = neighbors.union(get_neighbors(point, dirs))
    neighbors = neighbors.difference(active_points)
    for point in neighbors:
        if change_to_active(point, active_points):
            next_cycle_active.add(point)
    for point in active_points:
        if not change_to_inactive(point, active_points):
            next_cycle_active.add(point)
    active_points = set()
    active_points = active_points.union(next_cycle_active)

result1 = len(active_points)

#f.answer_a = result1
print('Solution 1st part:', result1)
