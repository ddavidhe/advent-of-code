from shapely import Polygon

pairs = []
with open('day9.txt', 'r') as file:
    for line in file:
        pairs.append(line.strip().split(','))

real_pairs = []
for i in range(len(pairs)):
    real_pairs.append([int(pairs[i][0]), int(pairs[i][1])])

# print(real_pairs)

def calculate_area(p1, p2):
    length = abs(p1[0] - p2[0]) + 1
    width = abs(p1[1] - p2[1]) + 1
    return length * width

p1 = 0
for i in range(len(real_pairs)):
    for j in range(len(real_pairs)):
        if i != j:
            p1 = max(p1, calculate_area(real_pairs[i], real_pairs[j]))

print(p1)

large_shape = Polygon(real_pairs)
p2 = 0

for i in range(len(real_pairs)):
    for j in range(len(real_pairs)):
        if i != j:
            bot_right = max(real_pairs[i][0], real_pairs[j][0])
            bot_left = min(real_pairs[i][0], real_pairs[j][0])
            top_right = max(real_pairs[i][1], real_pairs[j][1])
            top_left = min(real_pairs[i][1], real_pairs[j][1])

            rect = Polygon([(bot_left, top_left), (bot_right, top_left), (bot_right, top_right), (bot_left, top_right)])
            if large_shape.contains(rect):
                p2 = max(p2, calculate_area(real_pairs[i], real_pairs[j]))
print(p2)
