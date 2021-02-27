import copy
from pprint import pprint
from collections import deque
from data import inputGen

f = inputGen.getPuzzle(2020, 24)
file = f.input_data
file = file.split('\n')

dirs = {'e': (-2,0),'w': (2,0),'ne': (-1,1),'nw': (1,1),'se': (-1,-1),'sw': (1,-1)}

black = set()
for row in file:
    x, y = 0, 0
    r = list(row)
    while r:
        d = r.pop(0)
        if d not in 'ew':
            d += r.pop(0)
        x += dirs[d][0]
        y += dirs[d][1]
    if (x,y) in black:
        black.remove((x,y))
    else:
        black.add((x,y))

result1 = len(black)

for _ in range(100):
    new_black = set()
    for tile in black:
        count_for_black = 0
        x, y = tile
        for k1,v1 in dirs.items():
            x1 = x + v1[0]
            y1 = y + v1[1]
            if (x1,y1) in black:
                count_for_black += 1
            else:
                count_for_white = 0
                for k2,v2 in dirs.items():
                    x2 = x1 + v2[0]
                    y2 = y1 + v2[1]
                    if (x2,y2) in black:
                        count_for_white += 1
                if count_for_white == 2:
                    new_black.add((x1,y1))

        if 0 < count_for_black < 3:
            new_black.add(tile)
    black = new_black

result2 = len(new_black)

#f.answer_a = result1
#f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
