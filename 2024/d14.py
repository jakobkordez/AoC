from aoc import *
import re
from math import prod
from itertools import count
import numpy as np

data = read(14, ["\n", re.compile("-?\d+"), int])
W, H = 101, 103


def inQuad(x, y):
    if x == W // 2 or y == H // 2:
        return 0
    right = x > W // 2
    down = y > H // 2
    return right + (down << 1) + 1


p = [0] * 5
for x, y, dx, dy in data:
    x = (x + dx * 100) % W
    y = (y + dy * 100) % H
    p[inQuad(x, y)] += 1
print("Part 1:", prod(p[1:]))

for s in count():
    p = np.zeros((H, W), np.bool8)
    for x, y, dx, dy in data:
        x = (x + dx * s) % W
        y = (y + dy * s) % H
        p[y, x] = True
    score = np.count_nonzero(p[:-1, 1:-1] * (p[1:, 2:] | p[1:, :-2]))
    if score > 200:
        break
print("Part 2:", s)
