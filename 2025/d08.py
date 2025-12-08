from aoc import *
from math import prod
from time import time

data = read(8, ["\n", ",", int])
n = len(data)


def distance(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(3))


arr = sorted(
    (distance(data[i], data[j]), i, j) for i in range(n) for j in range(i + 1, n)
)

g = [{a} for a in range(n)]


def it(i, j):
    for gi in range(len(g)):
        if i in g[gi]:
            break
    for gj in range(len(g)):
        if j in g[gj]:
            break
    if gi == gj:
        return
    g[gi] |= g[gj]
    g.pop(gj)


for _, i, j in arr[:1000]:
    it(i, j)

print("Part 1:", prod(sorted(map(len, g))[-3:]))

for _, i, j in arr[1000:]:
    it(i, j)
    if len(g) == 1:
        break

print("Part 2:", data[i][0] * data[j][0])
