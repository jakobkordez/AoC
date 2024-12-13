from aoc import *
import re

data = read(13, ["\n\n", re.compile(r"\d+"), int])


def solve(ax, ay, bx, by, x, y):
    b = ((x * ay) - (y * ax)) / ((bx * ay) - (by * ax))
    a = (x - b * bx) / ax
    if b % 1 != 0 or a % 1 != 0 or b < 0 or a < 0:
        return 0
    return int(b) + 3 * int(a)


print("Part 1:", sum(solve(*d) for d in data))
print(
    "Part 2:",
    sum(solve(*d[:4], d[4] + 10000000000000, d[5] + 10000000000000) for d in data),
)
