import csv

with open('data.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter=' ')
    list1 = []
    list2 = []

    for row in reader:
        list1.append(int(row[0]))
        list2.append(int(row[3]))

similarity = 0

for i in list1:
    freq = 0
    for j in list2:
        if (i == j):
            freq += 1
    
    similarity += i * freq

print(similarity)

