from data import inputGen

f = inputGen.getPuzzle(2020, 5)
file = f.input_data
file = file.split()

ids = []
for line in file:
    a=''
    for i in line:
        a += '0' if i in 'FL' else '1'
    id =int(a[:7],2)*8 + int(a[7:],2)
    ids.append(id)
ids.sort()
result1 = ids[-1]
for num in range(ids[0],ids[-1]):
    if num not in ids:
        result2 = num
        break

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
