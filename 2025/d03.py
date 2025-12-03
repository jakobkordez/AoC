from aoc import *

data = read(3, ["\n", list, int])


def maxIndex(p):
    m = mi = -1
    for i, v in enumerate(p):
        if v > m:
            m = v
            mi = i
    return mi


def solve(b, n):
    d = [-1] * n
    for di in range(n):
        i = d[di - 1] + 1
        e = -n + di + 1
        d[di] = maxIndex(b[i : e if e < 0 else None]) + i
    return int("".join(str(b[dd]) for dd in d))


def solvePart(n):
    return sum(solve(b, n) for b in data)


print("Part 1:", solvePart(2))
print("Part 2:", solvePart(12))
