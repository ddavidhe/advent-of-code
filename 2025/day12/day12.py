with open('day12.txt', 'r') as f:
    shapes = f.read().split('\n')

with open('day12two.txt', 'r') as f:
    grids = f.read().split('\n')

shape_sizes = {}

cur_index = 0
cur_size = 0
for s in shapes:
    if ':' in s:
        temp = s.index(':')
        cur_index = int(s[:temp])
    elif s == '':
        shape_sizes[cur_index] = cur_size
        cur_size = 0
    else:
        # must be a hashtag thing
        cur_size += s.count('#')
shape_sizes[cur_index] = cur_size

print(shape_sizes)


grid_info = []
for g in grids:
    source = g.split(':')
    trash1 = (source[0].split('x'))
    dimensions = []
    for t in trash1:
        dimensions.append(int(t))

    required = source[1].split(' ')
    required.pop(0)
    for i in range(len(required)):
        required[i] = int(required[i])

    grid_info.append((dimensions, required))

p1 = 0
for setup in grid_info:
    tiles = setup[0][0] * setup[0][1]
    hashtags = 0
    for i in range(len(setup[1])):
        print(setup)
        hashtags += setup[1][i]*shape_sizes[i]
    if tiles >= hashtags:
        p1 += 1

print(p1)