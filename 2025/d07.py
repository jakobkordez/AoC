from aoc import *
from functools import cache

data = read(7, ["\n", list])
p1 = 0


@cache
def solve(y, x):
    if y >= len(data):
        return 1
    if data[y][x] == "^":
        global p1
        p1 += 1
        return solve(y, x - 1) + solve(y, x + 1)
    return solve(y + 1, x)


p2 = solve(1, data[0].index("S"))
print("Part 1:", p1)
print("Part 2:", p2)
