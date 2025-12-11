from functools import cache

with open('day11.txt', 'r') as f:
    data = f.read().split('\n')

adjacency_list = {}
for thing in data:
    temp = thing.split(':')
    temp_arr = []
    for item in temp[1].split(' '):
        if item != '':
            temp_arr.append(item)
    adjacency_list[temp[0]] = temp_arr

p1 = 0

def dfs(graph, start):
    global p1

    if start == 'out':
        p1 += 1
    
    for neighbour in graph.get(start, []):
        dfs(graph, neighbour)

dfs(adjacency_list, 'you')
print(p1)

# part 2

@cache
def dfs2(start, seenFFT, seenDAC):
    if start == 'out':
        if seenFFT and seenDAC:
            return 1
        return 0

    t = 0
    for neighbour in adjacency_list.get(start, []):
        if neighbour == 'fft':
            t += dfs2(neighbour, True, seenDAC)
        elif neighbour == 'dac':
            t += dfs2(neighbour, seenFFT, True)
        else:
            t += dfs2(neighbour, seenFFT, seenDAC)
    return t

p2 = dfs2('svr', False, False)
print(p2)