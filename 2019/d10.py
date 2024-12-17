from aoc import *
from math import gcd
from collections import defaultdict

data = read(10, ["\n", list])

ast = []
for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c != "#":
            continue
        ast.append((x, y))


def shrink(dx, dy):
    g = gcd(dx, dy)
    if g == 0:
        return (0, 0)
    return (dx // g, dy // g)


best = 0
for ax, ay in ast:
    s = defaultdict(lambda: [])
    for bx, by in ast:
        s[shrink(bx - ax, by - ay)].append((bx, by))
    del s[(0, 0)]
    if len(s) > best:
        best = len(s)
        bMap = s
        for a in bMap.values():
            a.sort(key=lambda p: abs(p[0] - ax) + abs(p[1] - ay), reverse=True)


print("Part 1:", best)


def getK(x, y):
    if x == 0:
        return y * 99999999
    return y / x


pp = sorted(bMap, key=lambda c: (c[0] < 0, getK(*c)))

i = 0
for a in range(200):
    while bMap[pp[i % len(pp)]] == []:
        i += 1
    x, y = bMap[pp[i % len(pp)]].pop()
    i += 1

print("Part 2:", x * 100 + y)
