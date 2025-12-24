from aoc import *
from math import prod
import numpy as np
import sys

sys.setrecursionlimit(15000000)

data = read(9, ["\n", ",", int])
n = len(data)

print(
    "Part 1:",
    max(
        prod(abs(a - b) + 1 for a, b in zip(a, b))
        for i, a in enumerate(data)
        for b in data[i + 2 :]
    ),
)


def m(arr):
    return {e: (i + 1) * 2 for i, e in enumerate(sorted(set(arr)))}


dim = 500

xmp, ymp = map(m, zip(*data))
p = np.zeros((dim, dim), dtype=np.int_)
for (ax, ay), (bx, by) in zip(data, roll(data, 1)):
    l, r = sorted((xmp[ax], xmp[bx]))
    b, t = sorted((ymp[ay], ymp[by]))
    p[b : t + 1, l : r + 1] = 1


def ff(y, x):
    if y < 0 or y >= dim or x < 0 or x >= dim:
        return
    if p[y, x] != 0:
        return
    p[y, x] = -1
    for dy, dx in FOUR_NEIGHBOURS:
        ff(y + dy, x + dx)


ff(0, 0)
p = p >= 0

mx = 0
for i, (ax, ay) in enumerate(data):
    for bx, by in data[i + 1 :]:
        l, r = sorted((xmp[ax], xmp[bx]))
        b, t = sorted((ymp[ay], ymp[by]))
        if p[b : t + 1, l : r + 1].all():
            mx = max(mx, (abs(ax - bx) + 1) * (abs(ay - by) + 1))
print("Part 2:", mx)
