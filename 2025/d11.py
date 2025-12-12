from aoc import *
import re
from functools import cache

data = {d: n for d, *n in read(11, ["\n", re.compile(r"\w+")])}
data["out"] = []


@cache
def solve(s, t):
    if s == t:
        return 1
    return sum(solve(pt, t) for pt in data[s])


print("Part 1:", solve("you", "out"))
print("Part 2:", solve("svr", "fft") * solve("fft", "dac") * solve("dac", "out"))
