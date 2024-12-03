import csv

with open('data.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter=' ')
    list1 = []
    list2 = []

    for row in reader:
        list1.append(int(row[0]))
        list2.append(int(row[3]))

list1.sort()
list2.sort()

differences = []

for i in range(len(list1)):
    differences.append(abs(list2[i] - list1[i]))

sum = 0
for i in range(len(differences)):
    sum += differences[i]

print(sum)