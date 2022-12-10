import math
f = open('/Users/bas/GIT/aoc2022/day10/input.txt', 'r')

ins = []

for val in f:
    val = val.strip().split(' ')
    if len(val) > 1:
        val[1] = int(val[1])
    ins.append(val)


def part1(ins):
    ex = 1
    x = 1
    resList = [20, 60, 100, 140, 180, 220]
    res = []

    for i, val in enumerate(ins):
        if ex in resList:
            res.append(x * ex)
        if val[0] == 'noop':
            ex += 1
        elif val[0] == 'addx':
            ex += 1
            if ex in resList:
                res.append(x * ex)
            ex += 1
            x += val[1]
    return sum(res)


pixels = []
x = 1
cx = 0
for val in ins:
    if val[0] == 'noop':
        if cx % 40 >= x - 1 and cx % 40 <= x + 1:
            pixels.append(cx)
        cx += 1
    elif val[0] == 'addx':
        if cx % 40 >= x - 1 and cx % 40 <= x + 1:
            pixels.append(cx)
        cx += 1
        if cx % 40 >= x - 1 and cx % 40 <= x + 1:
            pixels.append(cx)
        cx += 1
        x += val[1]

screen = [[' ' for i in range(40)] for x in range(6)]

for val in pixels:
    screen[math.floor(val / 40)][val % 40] = '#'


print('part 1:', part1(ins))
print('part 2:')
for val in screen:
    print(' '.join(val))
