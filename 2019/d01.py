from aoc import *

data = read(1, ["\n", int])

print("Part 1:", sum(v // 3 - 2 for v in data))


def f(x):
    if x <= 0:
        return 0
    return x + f(x // 3 - 2)


print("Part 2:", sum(f(v) - v for v in data))
