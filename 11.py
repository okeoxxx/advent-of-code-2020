import copy
from data import inputGen

f = inputGen.getPuzzle(2020, 11)
file = f.input_data
file = file.split()

grid = []
grid_part2 = []
for row in file:
    grid.append(list(row))
    grid_part2.append(list(row))

def count_neighbor(grid, i, j, part2=0):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    
    for d in dirs:
        lenght = 1
        while True:
            x, y = i + lenght * d[0], j + lenght * d[1]
            if x < 0 or y < 0:
                break
            try:
                if grid[x][y] == '#':
                    count += 1
                    break
                elif grid[x][y] == 'L':
                    break
                if part2:
                    lenght += 1
                else:
                    break
            except IndexError:
                break
    return count

a = 0
trigger = True
while trigger:
    trigger = False
    new_grid = copy.deepcopy(grid)
    for i, row in enumerate(grid):
        for j, seat in enumerate(row):
            if seat == '.':
                continue
            if seat == '#':
                if count_neighbor(grid, i, j) >= 4:
                    new_grid[i][j] = 'L'
                    trigger = True
            else:
                if count_neighbor(grid, i, j) == 0:
                    new_grid[i][j] = '#'
                    trigger = True
    grid = copy.deepcopy(new_grid)

result1 = 0
for row in grid:
    result1 += row.count('#')

trigger = True
while trigger:
    trigger = False
    new_grid = copy.deepcopy(grid_part2)
    for i, row in enumerate(grid_part2):
        for j, seat in enumerate(row):
            if seat == '.':
                continue
            if seat == '#':
                if count_neighbor(grid_part2, i, j, part2=True) >= 5:
                    new_grid[i][j] = 'L'
                    trigger = True
            else:
                if count_neighbor(grid_part2, i, j, part2=True) == 0:
                    new_grid[i][j] = '#'
                    trigger = True
    grid_part2 = copy.deepcopy(new_grid)

result2 = 0
for row in grid_part2:
    result2 += row.count('#')

#f.answer_a = result1
#f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
