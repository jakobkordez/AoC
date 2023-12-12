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
    if sum(v) + len(v) - 1 > len(d):
        return 0
    c = 0
    if d[0] != "#":
        c += go(d[1:].strip("."), v)
    vv, *sv = v
    if d.find(".") % (len(d) + 1) < vv:
        return c
    if vv == len(d) or d[vv] != "#":
        c += go(d[vv + 1 :].strip("."), tuple(sv))
    return c


p1 = p2 = 0
for d, v in data:
    v = tuple(map(int, v.split(",")))
    p1 += go(d.strip("."), v)
    p2 += go("?".join([d] * 5).strip("."), tuple(chain(*repeat(v, 5))))

print("Part 1:", p1)
print("Part 2:", p2)
