import string

f = open('/Users/bas/GIT/aoc2022/day03/input.txt', 'r')
ff = open('/Users/bas/GIT/aoc2022/day03/input.txt', 'r')
f1 = f
part1 = []
part2 = []


def part1(file):
    res = []
    for i, val in enumerate(file):
        val = str(val)
        firstpart, secondpart = val[:len(val)//2], val[len(val)//2:]
        firstpart = [x for x in str(firstpart)]
        secondpart = [x for x in secondpart]

        matching = [val for val in firstpart if secondpart.count(val)]

        res.append(string.ascii_letters.index(matching[0]) + 1)

    return sum(res)


def part2(file):
    res = []
    res1 = []
    res2 = []

    for i, val in enumerate(file):
        val = val.strip()
        res1.append([x for x in val])
        if i % 3 == 2:
            res2.append(res1)
            res1 = []

    for i in res2:
        out = [x for x in i[0] if x in i[1] and x in i[2]]
        res.append(string.ascii_letters.index(out[0]) + 1)

    return sum(res)


part1 = part1(f)
part2 = part2(ff)

print('part 1: ' + str(part1))
print('part 2: ' + str(part2))
