from aoc import *

data = read(2, ["\n", " ", int])


def f(r):
    r = [b - a for a, b in zip(r, r[1:])]
    return all(e * r[0] > 0 and abs(e) <= 3 for e in r)


print("Part 1:", sum(map(f, data)))

print("Part 2:", sum(any(f(r[:i] + r[i + 1 :]) for i in range(len(r) + 1)) for r in data))
