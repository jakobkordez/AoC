from aoc import *
from functools import cache
from itertools import repeat, chain

data = read(12, ["\n", " "])


@cache
def go(d: str, v: tuple):
    if len(v) == 0:
        return 1 if "#" not in d else 0
    if d == "":
        return 0
    c = 0
    if d[0] != "#":
        c += go(d[1:].strip("."), v)
    vv, *sv = v
    i = d.find(".")
    if i == -1:
        i = len(d)
    if i < vv:
        return c
    if vv == len(d) or d[vv] != "#":
        c += go(d[vv + 1 :].strip("."), tuple(sv))
    return c


p1 = p2 = 0
for d, v in data:
    v = [*map(int, v.split(","))]
    p1 += go(d.strip("."), tuple(v))

    v = chain(*repeat(v, 5))
    p2 += go("?".join([d] * 5).strip("."), tuple(v))

print("Part 1:", p1)
print("Part 2:", p2)
