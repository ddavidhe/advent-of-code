ranges = []
with open('day5.txt', 'r') as file:
    for line in file:
        ranges.append(line.strip())

fruits = []
with open('day5two.txt', 'r') as file:
    for line in file:
        fruits.append(int(line.strip()))


num_fresh = 0

fresh_ranges = []
for r in ranges:
    start, end = map(int, r.split('-'))
    fresh_ranges.append((start, end))

fresh_ranges.sort(key=lambda x: x[0])

for i in range(len(fresh_ranges) - 1):
    current_start, current_end = fresh_ranges[i]
    next_start, next_end = fresh_ranges[i + 1]

    if next_start <= current_end:
        merged_end = max(current_end, next_end)
        fresh_ranges[i + 1] = (current_start, merged_end)
        fresh_ranges[i] = None

fresh_ranges = [r for r in fresh_ranges if r is not None]

for fruit in fruits:
    is_fresh = False
    for start, end in fresh_ranges:
        if start <= fruit <= end:
            is_fresh = True
            break
    if is_fresh:
        num_fresh += 1

print(num_fresh)

range_sum = 0
for r in fresh_ranges:
    start, end = r
    range_sum += (end - start + 1)
print(range_sum)