from data import inputGen

f = inputGen.getPuzzle(2020, 2)
file = f.input_data
file = file.split()

result1 = 0
result2 = 0

while file:
    passw = file.pop()
    char = file.pop()[0]
    policy = file.pop().split('-')
    cnt = passw.count(char)
    if int(policy[0]) <= cnt <= int(policy[1]):
        result1 += 1
    chars = [passw[int(policy[0])-1], passw[int(policy[1])-1]]
    if chars.count(char) == 1:
        result2 += 1

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
