import copy
from pprint import pprint
from collections import deque
from data import inputGen

f = inputGen.getPuzzle(2020, 23)
file = f.input_data
file = '389125467'
#file = file.split('\n')

cups = deque([x for x in map(int, list(file))])
def tick(cups, m):
    num = cups[0] - 1 if cups[0] != 1 else m
    cups.rotate(-1)
    while True:
        i = cups.index(num)
        if i < 3:
            num -= 1
            if num == 0:
                num = m
        else:
            break

    for _ in range(3):
        cups.insert(i, cups.popleft())
    return cups
for _ in range(100):
    tick(cups, 9)

while cups[0] != 1:
    cups.rotate(-1)

cups.popleft()
result1 = ''.join(list(map(str, cups)))

result2 = 0

#f.answer_a = result1
#f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
