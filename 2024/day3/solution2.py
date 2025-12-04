import csv
import re

masterMemory = ""

with open('data.csv', newline = None) as file:
    reader = csv.reader(file, delimiter='=') #= doesn't appear in the data lol

    for row in reader:
        masterMemory = masterMemory + str(row)

processedMemory = []

cut_up = masterMemory.split("do()")
for pieces in cut_up:
    # ok the idea is that every "piece" begins with do.
    # Then if I see don't i just stop.
    subSplit = pieces.split("don't",1)[0]
    processedMemory.append(subSplit)

total = 0
for i in processedMemory:
    pattern = r'mul\(\b\d{1,3}\b,\b\d{1,3}\b\)'
    matches = re.findall(pattern, i)

    for j in matches:
        num_pattern = r'\d{1,3}'
        nums = re.findall(num_pattern, j)
        product = int(nums[0]) * int(nums[1])
        total += product

print(total)