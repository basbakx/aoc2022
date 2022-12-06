f = open('/Users/bas/GIT/aoc2022/day06/input.txt', 'r')
f = list(f.read())


def func(f, l):
    list = [1, 1]
    i = 0
    while len(list) > len(set(list)):
        list = [f[list] for list in range(i, i + l) if i + l < len(f)]
        i += 1
    return i + l - 1


part1 = func(f, 4)
part2 = func(f, 14)

print('part 1: ' + str(part1))
print('part 2: ' + str(part2))
