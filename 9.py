from data import inputGen

f = inputGen.getPuzzle(2020, 9)
file = f.input_data
file = file.split()

block_size = 25
for i in range(block_size, len(file)):
    result1 = int(file[i])
    trigger = False
    block = list(map(int, file[i-block_size:i]))
    for block_part, num in enumerate(block):
        if (result1 - num) in block[block_part+1:]:
            trigger = True
            break
    if not trigger:
        break
result2 = 0
block = [int(file.pop(0))]

while not result2:
    if sum(block) == result1:
        result2 = min(block) + max(block)
    elif sum(block) < result1:
        block.append(int(file.pop(0)))
    else:
        block.pop(0)


f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
