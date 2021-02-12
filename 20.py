import copy
from pprint import pprint
from collections import deque
from data import inputGen

f = inputGen.getPuzzle(2020, 20)
file = f.input_data
file = file.split('\n')

tiles = dict()
edges = dict()

def rot_90(grid, c=1):
    l = []
    for g in grid:
        l.append(list(g))
    if c == 0:
        return grid
    elif c == 1:
        return [''.join(list(reversed(x))) for x in zip(*l)]
    else:
        return rot_90([''.join(list(reversed(x))) for x in zip(*l)], c - 1)

def get_edges(grid):
    rotated_grid = rot_90(grid)
    return [grid[0], rotated_grid[-1][::-1], grid[-1][::-1], rotated_grid[0], grid[0][::-1], rotated_grid[0][::-1], grid[-1], rotated_grid[-1]]

num = False

for row in file:
    if row == '':
        continue
    elif 'Tile' in row:
        if num:
            tiles[num] = piece
            edges[num] = get_edges(piece)
        num = row[5:-1]
        piece = []
    else:
        piece.append(row)

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def flip_x(piece):
    return [row[::-1] for row in piece]

def flip_y(piece):
    return piece[::-1]

def rotate_piece(d, i, piece):
    koef = (i + d + 2) % 4
    new_piece = rot_90(piece, koef)
    if d == 3:
        if i in  [0, 2]:
            return flip_y(new_piece)
    elif d == 2 and i == 0:
        return flip_x(new_piece)
    if i < 4:
        if d % 2 == 0:
            return flip_y(new_piece)
        else:
            return flip_x(new_piece)
    else:
        return new_piece

placed_tiles = dict()
placed_tiles[num] = [[0,0], get_edges(piece)[:4], piece]

while edges:
    change = False
    for num, value in placed_tiles.items():
        center_edges = value[1]
        for side, edge in enumerate(center_edges):
            if edge == '':
                continue
            nums = []
            for id, e in edges.items():
                if id == num:
                    continue
                elif edge in e:
                    nums.append(id)
                    index = e.index(edge)
            if len(nums) == 1:
                trigg = True
                id = nums[0]
                x = value[0][0] + dirs[side][0]
                y = value[0][1] + dirs[side][1]
                new_piece = rotate_piece(side, index, tiles[id])
                new_edges = get_edges(new_piece)[:4]
                for j, d in enumerate(dirs):
                    x2 = x + d[0]
                    y2 = y + d[1]
                    for k1,v1 in placed_tiles.items():
                        if k1 == num:
                            continue
                        if v1[0] == [x2,y2]:
                            trigg = False
                            oposite_side = j + 2 if j < 2 else j - 2
                            if v1[1][oposite_side] == new_edges[j][::-1]:
                                placed_tiles[id] = [[x,y], new_edges, new_piece]
                                oposite_side = side + 2 if side < 2 else side - 2
                                placed_tiles[id][1][oposite_side] = ''
                                placed_tiles[num][1][side] = ''
                                del edges[id]
                                change = True
                        if change:
                            break
                if trigg:              
                    placed_tiles[id] = [[x,y], new_edges, new_piece]
                    oposite_side = side + 2 if side < 2 else side - 2
                    placed_tiles[id][1][oposite_side] = ''
                    placed_tiles[num][1][side] = ''
                    del edges[id]
                    change = True
            elif len(nums) == 0:
                placed_tiles[num][1][side] = ''
        if change:
            break

min_x = 0
min_y = 0
max_x = 0
max_y = 0

for k,v in placed_tiles.items():
    x = v[0][0]
    y = v[0][1]
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y
        
r = []
result1 = 1

def remove_edges(p):
    res = []
    for row in p[1:-1]:
        res.append(row[1:-1])
    return res

for y in range(max_y, min_y - 1,  -1):
    r.append([])
    for x in range(min_x, max_x + 1):
        for k,v in placed_tiles.items():
            if v[0] == [x,y]:
                if x in [min_x, max_x] and y in [min_y, max_y]:
                    result1 *= int(k)
                piece_center = remove_edges(v[2])
                if not r[-1]:
                    r[-1] = piece_center
                else:
                    for i, row in enumerate(piece_center):
                        r[-1][i] += row
                break

result = []
c = 0
for rows in r:
    for row in rows:
        result.append(row)
        c += row.count('#')

points = [(-1, 18), (0,19), (0,18), (0,17), (0,12), (0,11), (0,6), (0,5), (1,16), (1,13), (1,10), (1,7), (1,4), (1,1)]
m = 0
for sea in [result, flip_x(result), rot_90(result), rot_90(flip_x(result)), rot_90(result, 2), rot_90(flip_x(result), 2), rot_90(result, 3), rot_90(flip_x(result), 3)]:
    for i, row in enumerate(sea[1:-1], 1):
        for j, point in enumerate(row[:-19]):
            if point == '#':
                if all([sea[i+x][j+y] == '#' for x, y in points]):
                    m += 1
    if m:
        break

result2 = c - m * (len(points) + 1)

#f.answer_a = result1
#f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
