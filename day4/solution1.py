import csv

crossword = []

with open('data.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter='=') #= doesn't appear in the data lol

    for row in reader:
        crossword.append(row)

print(len(crossword)) # number of rows
print(len(crossword[0][0])) # number of columns
# its 140 x 140

cross_matrix = []
# re call that range(n) returns 0,1,...,n-2,n-1
for i in range(140):
    temp = []
    for j in range(140):
        cur_wor = crossword[i][0]
        temp.append(cur_wor[j])
        # print(temp)
    cross_matrix.append(temp)
print(cross_matrix[0][139])

# cross_matrix[0] is the first row
# cross_matrix[0][0] is the first element of the first row

# walk through my matrix.
# if i hit an X, search the 8 cardinal directions if they're in bound
# realize that if we can search Y and X, we can do that diag

for i in range(140):
    for j in range(140):
        coord = (i,j)
        