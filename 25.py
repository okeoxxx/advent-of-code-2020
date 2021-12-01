from data import inputGen

f = inputGen.getPuzzle(2020, 25)
file = f.input_data

file = file.split('\n')

def get_loopsize(num):
    value = 1
    subject_num = 7
    loop = 0
    while value % num != 0:
        value = value * subject_num % 20201227
        loop += 1
    return loop

def get_encryption_key(loop, public_key):
    value = 1
    while loop != 0:
        value = value * public_key % 20201227
        loop -= 1
    return value

result1 = get_encryption_key(get_loopsize(int(file[0])), int(file[1]))

#f.answer_a = result1
print('Solution 1st part:', result1)
