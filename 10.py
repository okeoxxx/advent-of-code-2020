from data import inputGen

f = inputGen.getPuzzle(2020, 10)
file = f.input_data
file = file.split()
file = list(map(int, file))
file.sort()

count_1jolt = 0
count_3jolt = 1
cur_num = 0
for num in file:
    dif = num - cur_num
    if dif == 1:
        count_1jolt += 1
    else:
        count_3jolt += 1
    cur_num = num

result1 = count_1jolt * count_3jolt

forks = []
possibilities = []
file.insert(0, 0)
for num in file[:-1]:
    fork = 0
    for i in range(1, 4):
        if num + i in file:
            fork += 1
    forks.append(fork)
    possibilities.append(0)

possibilities.append(1)
while len(possibilities) > 1:
    num = possibilities.pop()
    for i in range(1, 4):
        try:
            if forks[-i] >= i:
                possibilities[-i] += num
        except IndexError:
            continue
    forks.pop()

result2 = possibilities.pop()

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
