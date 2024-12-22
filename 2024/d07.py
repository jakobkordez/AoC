from aoc import *
import re
from functools import cache

data = read(7, ["\n", re.compile(r"\d+"), int])


@cache
def p(b):
    a = 1
    while b > 0:
        a *= 10
        b //= 10
    return a


def solve(temp, i, a, target, part):
    if temp > target:
        return False
    if i == len(a):
        return temp == target
    return (
        (part and solve(temp * p(a[i]) + a[i], i + 1, a, target, part))
        or solve(temp + a[i], i + 1, a, target, part)
        or solve(temp * a[i], i + 1, a, target, part)
    )


p1 = p2 = 0
for res, *vals in data:
    if solve(vals[0], 1, vals, res, 0):
        p1 += res
    elif solve(vals[0], 1, vals, res, 1):
        p2 += res

print("Part 1:", p1)
print("Part 2:", p1 + p2)
