from data import inputGen

f = inputGen.getPuzzle(2020, 13)
file = f.input_data
file = file.split()

time = int(file[0])
bus_ids = []
delays =[]
for i, num in enumerate(file[1].split(',')):
    if num == 'x':
        continue
    else:
        bus_ids.append(int(num))
        delays.append(i%int(num))

lowest = [time, 0]

for id in bus_ids:
    waiting_time = id - time % id
    if lowest[0] > waiting_time:
        lowest = [waiting_time, id]

result1 = lowest[0] * lowest[1]

nums = [0, bus_ids[0]]

for num in range(1, len(bus_ids)):
    dif = nums[-1] - nums[-2]
    trigger = 0
    a = nums[-2]
    while True:
        a += dif
        if bus_ids[num] - a % bus_ids[num] == delays[num]:
            nums.append(a)
            trigger += 1
        if trigger == 2:
            break

result2 = nums[-2]

#f.answer_a = result1
#f.answer_b = result2
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
