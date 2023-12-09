from aoc import *

data = read(9, ["\n", " "], int)


def go(a):
    return a[-1] + go([b - a for a, b in zip(a, a[1:])]) if any(a) else 0


print("Part 1:", sum(go(a) for a in data))
print("Part 2:", sum(go(a[::-1]) for a in data))
