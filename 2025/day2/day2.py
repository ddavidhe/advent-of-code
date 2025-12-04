import csv

def break_ranges(ids):
    # ample input is '11-22', output should be [11,12]
    id1 = 0
    id2 = 0
    for c in ids:
        if c == '-':
            id1 = int(ids[:ids.index(c)])
            id2 = int(ids[ids.index(c)+1:])
            break
    return([id1, id2])

def validate(id):
    # we want to see if id is of the form XX where X is some arbitraty number. So 123123.
    # strategy: divide and mod by 10^n where n is half the length of the number
    id_str = str(id)
    if len(id_str) % 2 != 0:
        return False
    n = len(id_str) // 2

    first_half = id // (10**n)
    second_half = id % (10**n)
    return (first_half == second_half)

def validate_part2(id):
    # now we want to see if X is repeated at least twice, can be repeated more:
    # strategy: instead of cutting in half we'll cut as many times as possible (with no remainder)
    id_str = str(id)
    length = len(id_str)
    possible_lengths = []
    for i in range(1, length//2 + 1): # reminder that // is division with floor
        if length % i == 0:
            possible_lengths.append(i)
    
    # possible_lengths represent the possible length of the substrings
    # now we just check them all i guess..

    for sub_length in possible_lengths:
        num_repeats = length // sub_length
        substring = id_str[:sub_length]
        constructed = substring * num_repeats # spam substring and see if its the same
        if constructed == id_str:
            return True
    return False

ranges = []
with open('day2.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        ranges = row

p1 = 0
p2 = 0
for r in ranges:
    id_pairs = break_ranges(r)

    for i in range(id_pairs[0], id_pairs[1]+1):
        if validate(i):
            p1 += i
        if validate_part2(i):
            p2 += i
print(p1)
print(p2)