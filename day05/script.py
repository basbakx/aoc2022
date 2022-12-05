import re
f = open('/Users/bas/GIT/aoc2022/day05/input.txt', 'r')

crates = []
ins = []

switch = False

for i, val in enumerate(f):
    strip = val.strip()
    if strip == '':
        switch = True
    elif switch:
        ins.append(strip)
    else:
        crates.append(val)


def splitcrates(crates):
    crates.pop()
    newcrates = []
    for line in crates:
        chunks = [line[i:i+4] for i in range(0, len(line), 4)]

        chunks = [re.sub('\[|\]| |\n', '', i) for i in chunks]
        newcrates.append(chunks)

    result = []
    for i in range(len(newcrates[0])):
        result.append([])

    for val in newcrates:
        for i, j in enumerate(val):
            if j:
                result[i].append(j)

    return result


def doPart1(crate, ins):
    newcrates = crate
    for val in ins:
        for i in range(val[0]):
            newcrates[val[2] - 1].insert(0, newcrates[val[1] - 1][0])
            newcrates[val[1] - 1].pop(0)

    result = ''
    for i in newcrates:
        result += i[0]

    return (result)


def doPart2(crate, ins):
    newcrates = crate
    for val in ins:
        for i in range(val[0]):
            newcrates[val[2] - 1].insert(0,
                                         newcrates[val[1] - 1][val[0] - i - 1])
        for i in range(val[0]):
            newcrates[val[1] - 1].pop(0)

    result = ''
    for i in newcrates:
        result += i[0]

    return (result)


crates = splitcrates(crates)
ins = [re.split(' from | to ', i.replace('move ', '')) for i in ins]
ins = [[int(j) for j in i] for i in ins]

part1 = doPart1(crates, ins)
part2 = doPart2(crates, ins)

print('part 1: ' + str(part1))
print('part 2: ' + str(part2))
