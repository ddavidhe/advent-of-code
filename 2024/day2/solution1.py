import csv

reports = []

with open('data.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter=' ')

    for row in reader:
        numbers = [ int(x) for x in row ]
        reports.append(numbers)

safe = 0
for i in reports:
    fine = True

    inc = False
    dec = False
    for j in range(len(i)):
        k = j + 1
        if (k < len(i)):
            # safe differences
            step = abs(i[j] - i[k])
            if (step > 3) or (step == 0):
                fine = False
            # always increasing or decreasing
            if ((i[j] - i[k]) < 0):
                inc = True
            else:
                dec = True

    if (inc and dec):
        fine = False

    if (fine):
        safe += 1
        
print(safe)