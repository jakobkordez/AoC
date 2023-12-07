from aoc import *
from collections import Counter

data = read(7, ["\n", " "])

handOrder = [[5], [1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1, 1]]
order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def rank(a):
    return handOrder.index(sorted(Counter(a).values()))


def sort(a, b):
    av = rank(a[0])
    bv = rank(b[0])
    if av != bv:
        return bv - av
    for i in range(5):
        aa = order.index(a[0][i])
        bb = order.index(b[0][i])
        if aa != bb:
            return bb - aa
    return 0


def solve(data):
    return sum((i + 1) * int(v) for i, (_, v) in enumerate(qsorted(data, sort)))


print("Part 1:", solve(data))

order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def rank(a):
    a = [c for c in a if c != "J"]
    if len(a) == 0:
        return 0
    c = sorted(Counter(a).values())
    c[-1] += 5 - len(a)
    return handOrder.index(c)


print("Part 2:", solve(data))
