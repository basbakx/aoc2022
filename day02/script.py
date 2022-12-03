f = open('/Users/bas/GIT/aoc2022/day02/input.txt', 'r')
lines = []
totalVal = 0


def compare(a, b):
    if a == 'X':
        i = 1
        if b == 'A':
            i += 3
        elif b == 'B':
            i += 0
        elif b == 'C':
            i += 6
    elif a == 'Y':
        i = 2
        if b == 'A':
            i += 6
        elif b == 'B':
            i += 3
        elif b == 'C':
            i += 0
    elif a == 'Z':
        i = 3
        if b == 'A':
            i += 0
        elif b == 'B':
            i += 6
        elif b == 'C':
            i += 3
    return i


def outcome(a, b):
    i = 'X'
    if a == 'X':
        if b == 'A':
            i = 'Z'
        elif b == 'B':
            i = 'X'
        elif b == 'C':
            i = 'Y'
    elif a == 'Y':
        if b == 'A':
            i = 'X'
        elif b == 'B':
            i = 'Y'
        elif b == 'C':
            i = 'Z'
    elif a == 'Z':
        if b == 'A':
            i = 'Y'
        elif b == 'B':
            i = 'Z'
        elif b == 'C':
            i = 'X'
    return i


part1 = 0
part2 = 0

for i, val in enumerate(f):
    val = val.strip().split(' ')
    part1 += compare(val[1], val[0])
    part2 += compare(outcome(val[1], val[0]), val[0])

print('part 1: ' + str(part1))
print('part 2: ' + str(part2))
