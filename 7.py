from data import inputGen

f = inputGen.getPuzzle(2020, 7)
file = f.input_data
file = file.split('\n')

#print(file)
d = dict()

looking_for = 'shiny gold'
suspect_color = set()

for row in file:
    a, b = row.split(' bags contain')
    inside = list(map(lambda x: x.strip(' '), b.split(',')))
    for bag in inside:
        ls = bag.split(' ')
        if ls[0] == 'no':
            d[a] = 0
            continue
        d.setdefault(a, dict())
        count = int(ls[0])
        color = ls[1] + ' ' + ls[2]
        if color == looking_for or color in suspect_color:
            suspect_color.add(a)
        d[a][color] = count

trigger = len(suspect_color)
while trigger:
    for color in d:
        if d[color] == 0:
            continue
        for c in d[color]:
            if c in suspect_color:
                suspect_color.add(color)
    if len(suspect_color) > trigger:
        trigger = len(suspect_color)
    else:
        trigger = False

def count_bags(num, color):
    if d[color] == 0:
        return num
    else:
        sum = 0
        for c, n in d[color].items():
            sum += count_bags(n, c)
        return num + num * sum

result1 = len(suspect_color)
result2 = count_bags(1, looking_for) - 1 

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
