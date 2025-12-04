import csv

rotations = []
with open('day1.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        rotations.append(row[0])

# print(rotations)

# the dial starts by pointing at 50
# if the command is L, it rotates to the Left (subtract)
# if the command is R, it rotates to the Right (add)
# if the value < 0, it wraps to 99. The same can be said for > 99

curr_position = 50
num_zeros1 = 0
num_zeros = 0

for rotation in rotations:
    pass_zero = False
    direction = rotation[0]
    value = rotation[1:]

    for _ in range(int(value)):
        if direction == 'L':
            curr_position = (curr_position - 1 + 100) % 100
        else:
            curr_position = (curr_position + 1) % 100
        if curr_position == 0:
            num_zeros += 1
    if curr_position == 0:
        num_zeros1 += 1

print(num_zeros1)
print(num_zeros)


# 6547 is too high
# 6500 is too high