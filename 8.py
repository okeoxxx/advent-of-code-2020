import copy
from data import inputGen

f = inputGen.getPuzzle(2020, 8)
file = f.input_data
file = file.split()

cmds = []

while file:
    cmd, num = file.pop(0), int(file.pop(0))
    cmds.append([cmd, num])

#1st part
pos = 0
accumulator = 0
used_positions = []
while True:
    if pos not in used_positions:
        used_positions.append(pos)
    else:
        result1 = accumulator
        break
    cmd, num = cmds[pos]
    if cmd == 'acc':
        accumulator += num
        pos += 1
    elif cmd == 'jmp':
        pos += num
    elif cmd == 'nop':
        pos += 1

#2nd part
for i, cmd in enumerate(cmds):
    if cmd[0] == 'acc':
        continue
    else:
        new_cmds = copy.deepcopy(cmds)
        new_cmds[i] = ['jmp', cmd[1]] if cmd[0] == 'nop' else ['nop', cmd[1]]
        pos = 0
        accumulator = 0
        used_positions = []
        trigger = False
        while True:
            if pos >= len(cmds):
                result2 = accumulator
                trigger = True
                break
            elif pos not in used_positions:
                used_positions.append(pos)
            else:
                break
            cmd, num = new_cmds[pos]
            if cmd == 'acc':
                accumulator += num
                pos += 1
            elif cmd == 'jmp':
                pos += num
            elif cmd == 'nop':
                pos += 1
        if trigger:
            break

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
