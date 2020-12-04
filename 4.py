from data import inputGen

f = inputGen.getPuzzle(2020, 4)
file = f.input_data
file = file.split('\n')

result1 = 0
result2 = 0
id = []

def check_valid_part2(id):
    for i in id:
        p, value = i.split(':')
        if p == 'byr' and (int(value) > 2002 or int(value) < 1920):
            return False
        elif p == 'iyr' and (int(value) > 2020 or int(value) < 2010):
            return False
        elif p == 'eyr' and (int(value) > 2030 or int(value) < 2020):
            return False
        elif p == 'hgt':
            unit = value[-2:]
            if unit not in ['cm', 'in']:
                return False
            val = int(value[:-2])
            if unit == 'cm':
                if val > 193 or val < 150:
                    return False
            elif unit == 'in':
                if val > 76 or val < 59:
                    return False
        elif p == 'hcl':
            valid_set = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
            if value[0] != '#' or len(value) != 7:
                return False
            for v in value[1:]:
                if v not in valid_set:
                    return False
        elif p == 'ecl' and value not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            return False
        elif p == 'pid':
            valid_set = {'0','1','2','3','4','5','6','7','8','9'}
            if len(value) != 9:
                return False
            for v in value:
                if v not in valid_set:
                    return False
    return True

def check_valid(id):
    valid_sets = [{'byr', 'iyr', 'eyr', 'ecl', 'pid', 'hcl', 'hgt', 'cid'}, {'byr', 'iyr', 'eyr', 'ecl', 'pid', 'hcl', 'hgt'}]
    global result2
    params = set()
    for i in id:
        param = i.split(':')[0]
        params.add(param)
    if params in valid_sets:
        if check_valid_part2(id):
            result2 += 1
        return True
    else:
        return False

for p in file:
    if p.strip(' ') == '':
        if check_valid(id):
            result1 += 1
        id = []
    else:
        id += (p.strip(' ').split())

if check_valid(id):
    result1 += 1

f.answer_a = result1
f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
