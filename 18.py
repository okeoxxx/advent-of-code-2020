import copy
from pprint import pprint
from collections import deque
from data import inputGen

f = inputGen.getPuzzle(2020, 18)
file = f.input_data
file = file.split('\n')
#print(file)

def calculate(string):
    string = string.strip('()')
    while string.count('*') + string.count('+') > 1:
        c = 0
        temp_s = ''
        for i, s in enumerate(string):
            if s in '+*':
                c += 1
            if c == 2:
                temp_s = eval(temp_s)
                string = str(temp_s) + string[i:]
                break
            else:
                temp_s += s
    return eval(string)

def calculate_part2(string):
    string = string.strip('()')
    temp_s = ''
    while True:
        i = string.find('*')
        if i == -1:
            temp_s += str(eval(string))
            break
        temp_s += str(eval(string[:i])) + '*'
        string = string[i+1:]
    return eval(temp_s)

result1 = 0
result2 = 0

for r in file:
    r2 = r
    while ')' in r:
        i2_1 = r.find(')') + 1
        i1_1 = r[:i2_1].rfind('(')
        i2_2 = r2.find(')') + 1
        i1_2 = r2[:i2_2].rfind('(')
        r = r[:i1_1] + str(calculate(r[i1_1:i2_1])) + r[i2_1:]
        r2 = r2[:i1_2] + str(calculate_part2(r2[i1_2:i2_2])) + r2[i2_2:]
    result1 += calculate(r)
    result2 += calculate_part2(r2)

#f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
