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

# we can just stop at every 'A', and check the corners
# check to see if the upper left corner is X and the bottom right is S, or vice versal
# do the same for the upper right and bottom left
# if both are true then we can add it

counter = 0
for i in range(1,139):
    for j in range(1,139):
        if cross_matrix[i][j] == 'A':
            word1 = (cross_matrix[i-1][j-1] + 'A' + cross_matrix[i+1][j+1])
            word2 = (cross_matrix[i-1][j+1] + 'A' + cross_matrix[i+1][j-1])

            if (word1 == 'SAM' or word1 == 'MAS') and (word2 == 'SAM' or word2 == 'MAS'):
                counter += 1
print(counter)