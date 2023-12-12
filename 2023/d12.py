from aoc import *
from functools import cache
from itertools import repeat, chain

data = read(12, ["\n", " "])


@cache
def go(d: str, v: str):
    if v == "":
        return 1 if "#" not in d else 0
    if d == "":
        return 0
    c = 0
    if d[0] != "#":
        c += go(d[1:].strip("."), v)
    vv, sv = v.split(",", 1)
    vv = int(vv)
    if d.find(".") % (len(d) + 1) < vv:
        return c
    if vv == len(d) or d[vv] != "#":
        c += go(d[vv + 1 :].strip("."), sv)
    return c


p1 = p2 = 0
for d, v in data:
    v = f"{v},"
    p1 += go(d.strip("."), v)
    p2 += go("?".join([d] * 5).strip("."), v * 5)

print("Part 1:", p1)
print("Part 2:", p2)
