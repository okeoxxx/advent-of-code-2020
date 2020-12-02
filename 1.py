from itertools import permutations

from data import inputGen

f = inputGen.getPuzzle(2020, 1)
file = f.input_data
file = file.split()
perm = permutations(file, 2)

for num1, num2 in list(perm):
    sum = int(num1) + int(num2)
    if sum == 2020:
        result1 = int(num1) * int(num2)
        break

perm2 = permutations(file, 3)

for num1, num2, num3 in list(perm2):
    sum = int(num1) + int(num2) + int(num3)
    if sum == 2020:
        result2 = int(num1) * int(num2) * int(num3)
        break

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
