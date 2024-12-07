from aoc import *
import re

data = read(7, ["\n", re.compile(r"\d+"), int])


def concat(a, b):
    # return int(f"{a}{b}")
    t = b
    while t > 0:
        a *= 10
        t //= 10
    return a + b


def solve(temp, i, a, target, part):
    if temp > target:
        return False
    if i == len(a):
        return temp == target
    return (
        solve(temp + a[i], i + 1, a, target, part)
        or solve(temp * a[i], i + 1, a, target, part)
        or (part and solve(concat(temp, a[i]), i + 1, a, target, part))
    )


print("Part 1:", sum(res for res, *vals in data if solve(vals[0], 1, vals, res, 0)))
print("Part 2:", sum(res for res, *vals in data if solve(vals[0], 1, vals, res, 1)))
