from aoc import *
import re
from functools import cache
from collections import defaultdict


inputs, gates = read(24, ["\n\n", "\n", re.compile("\w+")])


id = dict()
for k, v in inputs:
    id[k] = int(v)

gd = dict()
dg = defaultdict(lambda: [])
for a, g, b, c in gates:
    gd[c] = (a, g, b)
    dg[a].append(c)
    dg[b].append(c)


@cache
def go(c):
    if c in id:
        return id[c]
    a, g, b = gd[c]
    a = go(a)
    b = go(b)
    match g:
        case "AND":
            return a & b
        case "OR":
            return a | b
        case "XOR":
            return a ^ b


print("Part 1:", sum(2 ** int(k[1:]) for k in gd if k[0] == "z" and go(k)))


last = max(gd)


@cache
def gateType(c):
    a, g, b = gd[c]
    if g == "OR":
        return 5
    ipts = a[0] + b[0]
    if (ipts == "xy" or ipts == "yx") and g == "AND":
        return 1
    if (ipts == "xy" or ipts == "yx") and g == "XOR":
        return 2
    if g == "AND":
        return 3
    if g == "XOR":
        return 4
    return 0


def validate(c):
    if c == last or gd[c][0][1:] == "00":
        return True
    v = gateType(c)
    ch = list(map(gateType, dg[c]))
    match v:
        case 4:
            return c[0] == "z"
        case 1 | 3:
            return ch == [5]
        case 4:
            return ch == []
        case 2 | 5:
            return sorted(ch) == [3, 4]
    return False


print("Part 2:", ",".join(sorted(g for g in gd if not validate(g))))
