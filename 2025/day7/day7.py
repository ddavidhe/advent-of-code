rows = []
with open('sample.txt', 'r') as file:
    for line in file:
        rows.append(line.strip())

massive = []
memo = []

for r in rows:
    middle = []
    memo_middle = []
    for c in r:
        middle.append(c)
        memo_middle.append(-1)
    massive.append(middle)
    memo.append(memo_middle)

# create a dp function. dp(r,c) calculates number of splits from a beam that starts at position massive[r][c]
# the solution will be dp(0, massive[0].index('S'))
# the base case is if r goes past the last row, or if c goes past left or right
    # formally, r > len(massive)-1 or c < 0 or c > len(massive[0]) - 1
# if called and the (r,c) is a ., we just call (r+1,c)
# if called and the (r,c) is a splitter, we call (r+1, c-1) and (r+1, c+1). add them

split_count = 0

def dp(r, c, massive, memo):
    global split_count

    if r > len(massive) - 1 or c < 0 or c > len(massive[0]) - 1:
        return 0
    if memo[r][c] != -1:
        return memo[r][c]
    if massive[r][c] == '.' or massive[r][c] == 'S':
        result = dp(r + 1, c, massive, memo)
    elif massive[r][c] == '^':
        split_count += 1
        result = 1 + dp(r, c - 1, massive, memo) + dp(r, c + 1, massive, memo)
    
    memo[r][c] = result
    return result

dp(0, massive[0].index('S'), massive, memo)
print("SPLITS: ", split_count)

print("BEAMS: ", 1 + memo[0][massive[0].index('S')])