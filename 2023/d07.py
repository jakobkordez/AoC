from aoc import *
from collections import Counter

data = read(7, ["\n", " "])

handOrder = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]
order = "23456789TJQKA"


def rank(a):
    return handOrder.index(sorted(Counter(a).values()))


def mp(a):
    return rank(a[0]), *map(order.index, a[0]), a[1]


def solve():
    return sum((i + 1) * int(v) for i, (*_, v) in enumerate(sorted(map(mp, data))))


print("Part 1:", solve())

order = "J23456789TQKA"


def rank(a):
    a = [c for c in a if c != "J"]
    if not a:
        return 6
    c = sorted(Counter(a).values())
    c[-1] += 5 - len(a)
    return handOrder.index(c)


print("Part 2:", solve())
