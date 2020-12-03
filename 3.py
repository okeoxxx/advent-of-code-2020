from data import inputGen

f = inputGen.getPuzzle(2020, 3)
file = f.input_data
file = file.split()
#print(file)

wide = len(file[0])

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
result2 = 1
for slope in slopes:
    res = 0
    pos = 0
    for i, row in enumerate(file):
        if i % slope[1] == 0:
            if pos >= wide:
                pos = pos - wide * (pos // wide)
            if row[pos] == '#':
                res += 1
            pos += slope[0]
    result2 *= res
    if slope == (3,1):
        result1 = res

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
