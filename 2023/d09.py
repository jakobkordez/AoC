from aoc import *

data = read(9, ["\n", " "], int)


def go(a):
    if all(e == 0 for e in a):
        return 0
    return a[-1] + go([b - a for a, b in zip(a, a[1:])])


print("Part 1:", sum(go(a) for a in data))
print("Part 2:", sum(go(a[::-1]) for a in data))
