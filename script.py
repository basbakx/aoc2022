f = open('/Users/bas/GIT/aoc2022/input.txt', 'r')
lines = []
totalVal = 0

for i, val in enumerate(f):
    val = val.strip()
    if val != '':
        totalVal += int(val)
    else:
        lines.append(totalVal)
        totalVal = 0

lines.append(totalVal)
lines.sort(reverse=True)

part1 = lines[0]

part2 = 0
for i in range(3):
    part2 += lines[i]


print('part 1: ' + str(part1))
print('part 2: ' + str(part2))
