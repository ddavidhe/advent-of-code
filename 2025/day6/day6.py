ranges = []
with open('sample.txt', 'r') as file:
    for line in file:
        ranges.append(line.strip())

temp = ranges[-1]
temp = temp.replace(" ", "")
num_formulas = len(temp)

massive = []
for r in ranges:
    massive.append(r.split())

for i in range(len(massive)-1):
    for j in range(num_formulas):
        massive[i][j] = int(massive[i][j])

p1 = 0
for i in range(len(massive[0])):
    command = []
    for j in range(len(massive)):
        command.append(massive[j][i])
    if command[-1] == '+':
        blank = 0
        for k in range(len(command)-1):
            blank += command[k]
        p1 += blank
    elif command[-1] == '*':
        blank = 1
        for k in range(len(command)-1):
            blank *= command[k]
        p1 += blank

# print(p1)

# -------------------------------
f = open('day6.txt').read().strip().split('\n')

def apply(nums, operation):
    # print(nums, operation)

    if operation == '+':
        return sum(nums)
    elif operation == '*':
        result = 1
        for num in nums:
            result *= num
        return result
    
operation_line = f[-1]
num_lines = len(f) - 1

res = 0
l, r = 0, 1
while r < len(operation_line):
    if operation_line[r] != ' ':
        operation = operation_line[l]
        nums = []
        for i in range(r-2, l-1, -1):
            curr = []
            for j in range(num_lines):
                if f[j][i] != ' ':
                    curr.append(f[j][i])
            nums.append(int(''.join(curr)))
        res += apply(nums, operation)
        l = r
        r += 1
    else:
        r += 1

op = operation_line[l]
nums = []
for i in range(r+1, l-1, -1):
    curr = []
    for j in range(num_lines):
        if f[j][i] != ' ':
            curr.append(f[j][i])
    nums.append(int(''.join(curr)))

res += apply(nums, op)

print(res)