import csv

joltages = []
with open('day3.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        joltages.append(row[0])

# p1 = 0
p2 = 0
for joltage in joltages: # each joltage is a number but also a string
    best = 0
    n = len(joltage)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         temp = int(joltage[i])*10 + int(joltage[j])
    #         best = max(best, temp)
    
    # p1 += best

    # first, we know it HAS to exist in the first len - 12 characater. this is so there are 11 leftover to make 12
    # find the max in that range

    best_joltage = 0
    prev_index = -1
    for v in range(1, 13):
        search_area = joltage[prev_index+1:n-(12-v)]
        leader = 0
        for element in search_area:
            leader = max(int(element), leader)
        leader_index = joltage.index(str(leader), prev_index+1)
        best_joltage = best_joltage * 10 + leader
        prev_index = leader_index
    
    p2 += best_joltage

print(p2)