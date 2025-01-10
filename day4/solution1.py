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

# cross_matrix[0] is the first row
# cross_matrix[0][0] is the first element of the first row

# walk through my matrix.
# if i hit an X, search the 8 cardinal directions if they're in bound
# realize that if we can search Y and X, we can do that diagonal line

counter = 0
for i in range(140):
    for j in range(140):
        up = True
        down = True
        left = True
        right = True
        upleft = True
        upright = True
        downleft = True
        downright = True

        if (j < 3):
            left = False
            upleft = False
            downleft = False
        if (j > 136):
            right = False
            upright = False
            downright = False
        if (i < 3):
            up = False
            upleft = False
            upright = False
        if (i > 136):
            down = False
            downleft = False
            downright = False
        
        if (cross_matrix[i][j] == 'X'):
            if (up):
                # extract the word upwards
                word = ''
                for k in range(4):
                    word += cross_matrix[i-k][j]
                    if word == 'XMAS':
                        counter += 1
            if (down):
                # extract the word downwards
                word = ''
                for k in range(4):
                    word += cross_matrix[i+k][j]
                    if word == 'XMAS':
                        counter += 1
            if (left):
                # extract the word leftwards
                word = ''
                for k in range(4):
                    word += cross_matrix[i][j-k]
                    if word == 'XMAS':
                        counter += 1
            if (right):
                # extract the word rightwards
                word = ''
                for k in range(4):
                    word += cross_matrix[i][j+k]
                    if word == 'XMAS':
                        counter += 1
            if (upleft):
                # extract the word upleft
                word = ''
                for k in range(4):
                    word += cross_matrix[i-k][j-k]
                    if word == 'XMAS':
                        counter += 1
            if (upright):
                # extract the word upright
                word = ''
                for k in range(4):
                    word += cross_matrix[i-k][j+k]
                    if word == 'XMAS':
                        counter += 1
            if (downleft):
                # extract the word downleft
                word = ''
                for k in range(4):
                    word += cross_matrix[i+k][j-k]
                    if word == 'XMAS':
                        counter += 1
            if (downright):
                # extract the word downright
                word = ''
                for k in range(4):
                    word += cross_matrix[i+k][j+k]
                    if word == 'XMAS':
                        counter += 1
print(counter)