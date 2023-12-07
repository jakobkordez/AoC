from aoc import *
from math import prod
import re

data = read(2, ["\n", ": ", re.compile(r"\d+ ?\w*"), " "])

d = {"red": 12, "green": 13, "blue": 14}

print("Part 1:", sum(all(int(v) <= d[k] for v, k in r) * int(g[0][0]) for g, r in data))

sm = 0

for _, r in data:
    d = {"red": 0, "green": 0, "blue": 0}
    for v, k in r:
        d[k] = max(d[k], int(v))
    sm += prod(d.values())

print("Part 2:", sm)
