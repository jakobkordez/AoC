from aoc import *
import re
from functools import cache

towels, patterns = read(19, ["\n\n", re.compile("[a-z]+")])


@cache
def solve(pattern: str):
    if pattern == "":
        return 1
    sm = 0
    for t in towels:
        if pattern.startswith(t):
            sm += solve(pattern[len(t) :])
    return sm


r = list(map(solve, patterns))
print("Part 1:", sum(map(bool, r)))
print("Part 2:", sum(r))
