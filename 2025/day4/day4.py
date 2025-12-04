import csv

grid = []
with open('day4.csv', newline = '\n') as file:
    reader = csv.reader(file, delimiter='?')

    janky_as_fuck = []
    for row in reader:
        n = len(row[0])
        janky_as_fuck = row[0]
        break
    grid.append(['.']*(n+2))

    temp = []
    temp.append('.')
    for c in janky_as_fuck:
        temp.append(c)
    temp.append('.')

    grid.append(temp)

    for row in reader:
        temp = []
        temp.append('.')
        for c in row[0]:
            temp.append(c)
        temp.append('.')
        grid.append(temp)

    grid.append(['.']*(n+2))
    
total = 0
repeat = True
while repeat:
    repeat = False
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[0])-1):
            current = grid[r][c]
            if current == '@':
                count = 0
                if grid[r-1][c-1] == '@':
                    count += 1
                if grid[r][c-1] == '@':
                    count+= 1
                if grid[r+1][c-1] == '@':
                    count+= 1
                if grid[r-1][c] == '@':
                    count+= 1
                if grid[r+1][c] == '@':
                    count+= 1
                if grid[r-1][c+1] == '@':
                    count+= 1
                if grid[r][c+1] == '@':
                    count+= 1
                if grid[r+1][c+1] == '@':
                    count+= 1
                if count < 4:
                    total += 1
                    grid[r][c] = '.'
                    repeat = True
print(total)