import copy
from pprint import pprint
from data import inputGen

f = inputGen.getPuzzle(2020, 21)
file = f.input_data
file = file.split('\n')

alergens = dict()
ingredients = []
risk_ingredients = set()

for line in file:
    ingred, alerg = line.split(' (contains ')
    ingred = ingred.split()
    alerg = alerg.strip(')').split(', ')
    ingredients.append(ingred)
    for a in alerg:
        risk_ingred = alergens.setdefault(a, set(ingred))
        alergens[a] = risk_ingred.intersection(set(ingred))

for _ in range(5):
    for k1, v1 in alergens.items():
        if len(v1) == 1:
            risk_ingredients = risk_ingredients.union(v1)
            for k2, v2 in alergens.items():
                if k1 == k2:
                    continue
                else:
                    alergens[k2] = v2.difference(v1)


pprint(risk_ingredients)
result1 = 0

for food in ingredients:
    for i in food:
        if i not in risk_ingredients:
            result1 += 1

result2 = ''

for v in sorted(alergens.items()):
    result2 += next(iter(v[1])) + ','

result2 = result2[:-1]

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
