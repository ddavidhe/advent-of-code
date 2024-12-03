import csv
import re

memory = []

with open('data.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter='=')

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
        print(nums)
        product = int(nums[0]) * int(nums[1])
        total += product

print(total)


def calculate(memory: str) -> int:
    """
    Calculate the sum of products from matches of 'mul(a,b)' in the input string.

    :param memory: The input string containing 'mul(a,b)' patterns.
    :return: int: The sum of the products of all matched pairs. Returns 0 if no matches are found.
    """
    re_pattern = r"mul\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\)"
    if matches := re.findall(re_pattern, memory):
        return sum(int(match[0]) * int(match[1]) for match in matches)
    return 0