import csv
import re

memory = []

with open('data.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter='=') #= doesn't appear in the data lol

    for row in reader:
        memory.append(row)


# print(memory)


# 1*1 + 9*3 + 4*5 + 4*3 = 1 + 27 + 20 + 12 = 60
total = 0
for i in memory:
    pattern = r'mul\(\b\d{1,3}\b,\b\d{1,3}\b\)'
    matches = re.findall(pattern, i[0])

    for j in matches:
        num_pattern = r'\d{1,3}'
        nums = re.findall(num_pattern, j)
        product = int(nums[0]) * int(nums[1])
        total += product

print(total)