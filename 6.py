from data import inputGen

f = inputGen.getPuzzle(2020, 6)
file = f.input_data
file = file.split('\n')

group = []
result1 = 0
result2 = 0

def count_group(group):
    questions = set()
    for g in group:
        questions = questions.union(set(g))
    #print(len(questions), questions)
    return len(questions)

def count_group_part2(group):
    questions = set(group.pop())
    for g in group:
        questions = questions.intersection(set(g))
    print(len(questions), questions)
    return len(questions)

for p in file:
    if p.strip(' ') == '':
        result1 += count_group(group)
        result2 += count_group_part2(group)
        group = []
    else:
        group += (p.strip(' ').split())

result1 += count_group(group)
result2 += count_group_part2(group)

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
