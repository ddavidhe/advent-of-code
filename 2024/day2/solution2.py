import csv

reports = []

with open('data.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter=' ')

    for row in reader:
        numbers = [ int(x) for x in row ]
        reports.append(numbers)

def isSafe(level):
    fine = True

    inc = False
    dec = False
    for j in range(len(level)):
        k = j + 1
        if (k < len(level)):
            # safe differences
            step = abs(level[j] - level[k])
            if (step > 3) or (step == 0):
                fine = False
            # always increasing or decreasing
            if ((level[j] - level[k]) < 0):
                inc = True
            else:
                dec = True

    if (inc and dec):
        fine = False

    return fine

def tryRemoval(level):
    for j in range(len(level)):
        new_arr = level[:j] + level[j+1:]
        if (isSafe(new_arr)):
            return True
    return False

safe = 0
for i in reports:
    if (isSafe(i)):
        safe += 1
    else:
        if (tryRemoval(i)):
            safe += 1
print(safe)