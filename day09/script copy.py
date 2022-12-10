import copy

f = open('/Users/bas/GIT/aoc2022/day09/input.txt', 'r')

ins = [val.strip().split(' ') for val in f]
ins = [[ins[i][0], int(ins[i][1])] for i in range(len(ins))]

dir = {
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1]
}

posses = [[] for x in range(11)]
result = {(0, 0)}
posYs = [[0, 0] for x in range(11)]

print(ins)


def moveHead(d):
    posYs[0][0] += dir[d][0]
    posYs[0][1] += dir[d][1]

    for i in range(1, 10):
        moveTail(i)

    app = copy.deepcopy(posYs[0])
    posses[0].append(app)


def moveTail(i):
    offset = [posYs[i-1][0] - posYs[i][0], posYs[i-1][1] - posYs[i][1]]

    if offset[0] < -1 or offset[0] > 1:
        posYs[i][0] += round(offset[0] / 2)
        if offset[1] < 0 or offset[1] > 0:
            posYs[i][1] += offset[1]
    elif offset[1] < -1 or offset[1] > 1:
        posYs[i][1] += round(offset[1] / 2)
        if offset[0] < 0 or offset[0] > 0:
            posYs[i][0] += offset[0]

    app = copy.deepcopy(posYs[i])
    posses[i].append(app)

    if i == 9:
        result.add((posYs[9][0], posYs[9][1]))


for inst in ins:
    for i in range(inst[1]):
        moveHead(inst[0])


def part2(list):
    resultfun = []
    for val in list:
        if val not in resultfun:
            resultfun.append(val)
    return resultfun


vis = part2(posses[9])

print(len(result))
