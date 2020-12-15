from data import inputGen

f = inputGen.getPuzzle(2020, 15)
file = f.input_data
file = file.split(',')

nums = list(map(int, file))

while len(nums) < 2020:
    if nums[-1] in nums[:-1]:
        for i, num in enumerate(reversed(nums[:-1]), 1):
            if num == nums[-1]:
                nums.append(i)
                break
    else:
        nums.append(0)

result1 = nums[-1]

numbers = dict()
i = 0
for num in list(map(int, file)):
    i += 1
    numbers[num] = [i, 0]

num = int(file[-1])

while i < 30000000:
    i += 1
    n = numbers.get(num, [0, 0])
    if n[1]:
        num = i - n[1] -1
        try:
            numbers[num] = [i, numbers[num][0]]
        except:
            numbers[num] = [i, 0]
    else:
        num = 0
        numbers[0] = [i, numbers[0][0]]

result2 = num

#f.answer_a = result1
#f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
