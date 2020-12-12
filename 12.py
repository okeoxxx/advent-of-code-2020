from data import inputGen

f = inputGen.getPuzzle(2020, 12)
file = f.input_data
file = file.split()

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
d = 0
x, y = 0, 0
for cmd in file:
    letter = cmd[0]
    num = int(cmd[1:])
    if letter == 'F':
        x += num * dirs[d][0]
        y += num * dirs[d][1]
    elif letter in 'LR':
        m = num // 90
        d = d + m if letter == 'R' else d - m
        if d < 0:
            d += 4
        elif d > 3:
            d -= 4
    else:
        cur_d = 'ESWN'.find(letter)
        x += num * dirs[cur_d][0]
        y += num * dirs[cur_d][1]
result1 = abs(x) + abs(y)

x, y = 0, 0
waypoint = [10, 1]
for cmd in file:
    letter = cmd[0]
    num = int(cmd[1:])
    if letter == 'F':
        x += num * waypoint[0]
        y += num * waypoint[1]
    elif letter in 'LR':
        m = num // 90
        if m in [1, 3]:
            waypoint.reverse()
            if letter == 'L':
                m = 1 if m == 3 else 3
            if m == 1:
                waypoint[1] = -waypoint[1]
            else:
                waypoint[0] = -waypoint[0]
        else:
            waypoint[0] = -waypoint[0]
            waypoint[1] = -waypoint[1]
    else:
        cur_d = 'ESWN'.find(letter)
        waypoint[0] += num * dirs[cur_d][0]
        waypoint[1] += num * dirs[cur_d][1]

result2 = abs(x) + abs(y)

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
