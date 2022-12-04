f = open('/Users/bas/GIT/aoc2022/day04/input.txt', 'r')

part1 = 0
part2 = 0

ranges = []
for i, val in enumerate(f):
    val = val.strip().split(',')
    val = [j.split('-') for j in val]
    val = [int(x) for y in val for x in y]
    ranges.append(val)

for j, i in enumerate(ranges):
    set1 = set(range(i[0], i[1] + 1))
    set2 = set(range(i[2], i[3] + 1))

    if set1.issubset(set2) or set2.issubset(set1):
        # print(j + 1)
        part1 += 1

    intersection = set1.intersection(set2)
    if intersection:
        part2 += 1


print('part 1: ' + str(part1))
print('part 2: ' + str(part2))
