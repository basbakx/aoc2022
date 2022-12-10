import operator
import numpy as np


f = open('/Users/bas/GIT/aoc2022/day09/input.txt', 'r')

ins = [val.strip().split(' ') for val in f]
ins = [[ins[i][0], int(ins[i][1])] for i in range(len(ins))]

dir = {
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1]
}


result = []

posY = [15, 15]

# def moveT(posT):
#     offset = list(map(operator.sub, posT, posY))

#     if abs(offset[0]) == 2:
#         posY[0] += offset[0] / 2
#         if abs(offset[1]) > 0:
#             posY[1] += offset[1]

#     if abs(offset[1]) == 2:
#         posY[1] += offset[1] / 2
#         if abs(offset[0]) > 0:
#             posY[0] += offset[0]

#     res = [round(posY[0]), round(posY[1])]
#     result.append(res)

posses = [[] for x in range(10)]
posYs = [[15, 15] for x in range(10)]


counter = 0


def moveT(posT):
    global counter
    offset = list(map(operator.sub, posT, posYs[counter]))

    if abs(offset[0]) == 2:
        posYs[counter][0] += offset[0] / 2
        if abs(offset[1]) > 0:
            posYs[counter][1] += offset[1]
    if abs(offset[1]) == 2:
        posYs[counter][1] += offset[1] / 2
        if abs(offset[0]) > 0:
            posYs[counter][0] += offset[0]

    res = [round(posYs[counter][0]), round(posYs[counter][1])]
    posses[counter].append(res)

    if counter < 9:
        counter += 1
        moveT(res)
    else:
        counter = 0


def moveH(ins):
    posT = [15, 15]
    c = 0
    for inn in ins:
        c += 1
        for i in range(inn[1]):
            posT = list(map(operator.add, posT, dir[inn[0]]))
            moveT(posT)


moveH(ins)

part1 = []
for val in result:
    if val not in part1:
        part1.append(val)


def part2(list):
    resultfun = []
    for val in list:
        if val not in resultfun:
            resultfun.append(val)
    return resultfun


vis = part2(posses[9])

posses = [[' ' for x in range(30)] for x in range(30)]

for val in vis:
    posses[val[0]][val[1]] = '#'

for val in posses:
    print(val)

print(len(vis))
