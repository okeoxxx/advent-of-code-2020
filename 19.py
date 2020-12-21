import copy
from data import inputGen

f = inputGen.getPuzzle(2020, 19)
file = f.input_data
file = file.split('\n')

nums = dict()

while True:
    line = file.pop(0)
    if line == '':
        break
    k, v = line.split(': ')
    if v[0] == '"':
        nums[k] = {v.strip('"')}
        continue
    value = v.split(' ')
    list_v = []
    cur_v = []
    for v in value:
        if v == '|':
            list_v.append(cur_v)
            cur_v = []
        else:
            cur_v.append(v)
    list_v.append(cur_v)
    nums[k] = list_v

while isinstance(nums['0'], list):
    for k, v in nums.items():
        if isinstance(v, set):
            continue
        else:
            if all(isinstance(x, set) for x in v):
                res = set()
                for s in v:
                    res = res.union(s)
                nums[k] = res
                continue
            for i, possibility in enumerate(v):
                try:
                    if all(isinstance(nums[num], set) for num in possibility):
                        res = ['']
                        for num in possibility:
                            new_res = []
                            for part1 in res:
                                for part2 in nums[num]:
                                    new_res.append(part1+part2)
                            res = copy.deepcopy(new_res)
                        v[i] = set(res)
                except KeyError:
                    continue


results = nums['0'].intersection(set(file))
rest = set(file).difference(results)

result1 = len(results)
result2 = result1

def check_11(text):
    global nums
    for c42 in nums['42']:
        if text.startswith(c42):
            for c31 in nums['31']:
                if text.endswith(c31):
                    if len(text) == len(c42 + c31):
                        return True
                    elif len(text) > len(c42 + c31):
                        return check_11(text[len(c42):-len(c31):])

def check_8_11(text):
    global nums
    for comb in nums['42']:
        if text.startswith(comb):
            if check_11(text[len(comb):]):
                return True
            return check_8_11(text[len(comb):])
    return False

for r in rest:
    if check_8_11(r):
        result2 += 1

#f.answer_a = result1
#f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
