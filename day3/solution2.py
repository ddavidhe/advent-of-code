import csv
import re

memory = []

with open('data.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter='=') #= doesn't appear in the data lol

    for row in reader:
        memory.append(row)


