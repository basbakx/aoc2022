

f = open('/Users/bas/GIT/aoc2022/day08/input.txt', 'r')

left = []
top = []
for i, val in enumerate(f):
    val = list(val.strip())
    left.append(val)

left = [[int(j) for j in i] for i in left]

results = []
for i, row in enumerate(left):
    j = 0
    maxVal = -1
    while maxVal <= 9 and j < len(row):
        if row[j] > maxVal:
            maxVal = row[j]
            results.append([i, j])
        j += 1

    j = len(row) - 1
    maxVal = -1
    while maxVal <= 9 and j >= 0:
        if row[j] > maxVal:
            maxVal = row[j]
            results.append([i, j])
        j -= 1

for i in range(len(left[0])):
    j = 0
    maxVal = -1
    while maxVal <= 9 and j < len(left) - 1:
        if left[j][i] > maxVal:
            maxVal = left[j][i]
            results.append([j, i])
        j += 1

    j = len(left) - 1
    maxVal = -1
    while maxVal <= 9 and j >= 0:
        if left[j][i] > maxVal:
            maxVal = left[j][i]
            results.append([j, i])
        j -= 1

part1 = len(set(tuple(i) for i in results))
part2 = 0
for y in range(len(left)):
    for x in range(len(left[y])):
        l = t = r = b = 1
        res = 0
        while (x - l) > 0 and left[y][x - l] < left[y][x]:
            l += 1
        while x + r < len(left[y]) - 1 and left[y][x + r] < left[y][x]:
            r += 1
        while y + t < len(left) - 1 and left[y + t][x] < left[y][x]:
            t += 1
        while y - b > 0 and left[y - b][x] < left[y][x]:
            b += 1
        if x != 0 and y != 0 and y < len(left) - 1 and x < len(left[y]) - 1:
            res = l * r * t * b
        if res > part2:
            part2 = res

print('part 1: ' + str(part1))
print('part 2: ' + str(part2))
