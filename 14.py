from itertools import product
from data import inputGen

f = inputGen.getPuzzle(2020, 14)
file = f.input_data
file = file.split('\n')

mem = dict()

for row in file:
    cmd, value = row.split(' = ')
    if cmd == 'mask':
        mask = value
    else:
        dec_num = "{0:b}".format(int(value)).zfill(36)
        res = ''
        for i, num in enumerate(mask):
            if num in '01':
                res += num
            else:
                res += dec_num[i]
        pos = cmd[4:-1]
        mem[pos] = int(res, 2)

result1 = 0

for k, v in mem.items():
    result1 += v

mem = dict()

for row in file:
    cmd, value = row.split(' = ')
    if cmd == 'mask':
        mask = value
    else:
        address = cmd[4:-1]
        dec_num = "{0:b}".format(int(address)).zfill(36)
        res = ''
        for i, num in enumerate(mask):
            if num in 'X1':
                res += num
            else:
                res += dec_num[i]
        comb = product([1, 0], repeat=res.count('X'))
        for c in list(comb):
            i = 0
            pos = ''
            for j, num in enumerate(res):
                if num == 'X':
                    pos += str(c[i])
                    i += 1
                else:
                    pos += res[j]
            mem[pos] = int(value)

result2 = 0

for k, v in mem.items():
    result2 += v

#f.answer_a = result1
#f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
