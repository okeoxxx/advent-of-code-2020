from pprint import pprint
from data import inputGen

f = inputGen.getPuzzle(2020, 16)
file = f.input_data
file = file.split('\n')

rules = dict()
possible_col = dict()
set_rules = set()
nearby_tickets = []
your_ticket = False
trigger = False

while file:
    line = file.pop(0)
    if line == '':
        line = file.pop(0)
        trigger = True
        continue
    if trigger:
        if not your_ticket:
            your_ticket = list(map(int, line.split(',')))
        else:
            nearby_tickets.append(list(map(int, line.split(','))))
    else:
        param, conditions = line.split(': ')
        nums = []
        for c in conditions.split(' or '):
            n = c.split('-')
            nums.append(range(int(n[0]), int(n[1])+1))
        cur_set_rules = set()
        for n in nums:
            for i in n:
                set_rules.add(i)
                cur_set_rules.add(i)
        rules[param] = cur_set_rules
        possible_col[param] = [1]*20 #20 = len(your_ticket), but not known at the moment

invalid_values = []
valid_tickets = []

for t in nearby_tickets:
    valid = True
    for value in t:
        if value not in set_rules:
            invalid_values.append(value)
            valid = False
    if valid:
        valid_tickets.append(t)

result1 = sum(invalid_values)

for t in valid_tickets:
    for i, value in enumerate(t):
        for k, v in rules.items():
            if value not in v:
                possible_col[k][i] = 0

order = ['']*len(your_ticket)
while '' in order:
    for k, v in possible_col.items():
        if sum(v) == 1:
            order[v.index(1)] = k
        else:
            for j in range(20):
                if order[j] != '':
                    possible_col[k][j] = 0

result2 = 1

for i, o in enumerate(order):
    if 'departure' in o:
        result2 *= your_ticket[i]

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
