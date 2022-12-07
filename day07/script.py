f = open('/Users/bas/GIT/aoc2022/day07/input.txt', 'r')

part1 = 0
part2 = 0

path = []
list = []

dirs = set()

lastDir = ''
for i, val in enumerate(f):
    val = val.strip().split(' ')

    if val[0] == '$':
        if val[1] == 'cd':
            if val[2] == '..':
                path.pop()
            else:
                path.append(val[2])

                dirs.update({''.join(path)})
    elif val[0] == 'dir':
        lastDir = val[1]
    else:
        file = ''.join(path)
        # print(str(file) + ' ' + str(val[1]) + ' ' + str(val[0]))
        list.append([file, [val[1], int(val[0])]])

# Make dict of directory names with sizes
fileDict = {}
for dir in dirs:
    for file in list:
        if dir in file[0]:
            if dir in fileDict:
                fileDict[dir] += file[1][1]
            else:
                fileDict.update({dir: file[1][1]})

# Solve part 1
part1 = 0
for val in fileDict:
    if fileDict[val] <= 100000:
        part1 += fileDict[val]

# Solve part 2
requiredSpace = 30000000 - (70000000 - fileDict['/'])

bigDir = {}
for val in fileDict:
    if fileDict[val] > requiredSpace:
        bigDir.update({val: fileDict[val]})

part2 = bigDir[min(bigDir, key=bigDir.get)]

print('part 1: ' + str(part1))
print('part 2: ' + str(part2))
