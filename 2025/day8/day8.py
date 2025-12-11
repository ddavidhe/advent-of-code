import math
with open('day8.txt', 'r') as f:
    data = f.read().strip().split('\n')

points = []
for pair in data:
    x, y, z = map(int, pair.split(','))
    points.append((x, y, z))

def distance(p1, p2):
    # we can just not use the sqrt since its comparisons
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

num_connections = 1000 # 10 is for sample data purpose
connections = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
            connections.append((distance(points[i], points[j]), points[i], points[j]))

connections.sort()

networks = []
remaining_points = set(points)
last = None

for i in range(num_connections):
    goodNetworks = []
    for network in networks:
        if connections[i][1] in network or connections[i][2] in network:
            goodNetworks.append(network)
    
    if len(goodNetworks) == 0:
        networks.append(set([connections[i][1], connections[i][2]]))
    elif len(goodNetworks) == 1:
        goodNetworks[0].add(connections[i][1])
        goodNetworks[0].add(connections[i][2])
    else:
        networks.remove(goodNetworks[1])
        goodNetworks[0].update(goodNetworks[1])

lengths = []
for n in networks:
    lengths.append(len(n))
top_three_lengths = sorted(lengths)[-3:]

p1 = math.prod(top_three_lengths)
print(p1)

# part 2
networks = []
remaining_points = set(points)
last = None

for c in connections:
    goodNetworks = []
    for network in networks:
        if c[1] in network or c[2] in network:
            goodNetworks.append(network)
    
    if len(goodNetworks) == 0:
        networks.append({c[1], c[2]})
    elif len(goodNetworks) == 1:
        goodNetworks[0].add(c[1])
        goodNetworks[0].add(c[2])
    else:
        networks.remove(goodNetworks[1])
        goodNetworks[0].update(goodNetworks[1])

    remaining_points.discard(c[1])
    remaining_points.discard(c[2])

    if len(remaining_points) == 0:
        last = c
        break

print(last)
print(last[1][0] * last[2][0])

# 5878257280 is too low

# 8133642976 is the answer ????