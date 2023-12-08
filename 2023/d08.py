from aoc import *
import re
from math import lcm

((instr,),), path = read(8, ["\n\n", "\n", re.compile(r"\w+")])


d = {}
for s, l, r in path:
    d[s] = (l, r)


def next(c, i):
    return d[c][instr[i % len(instr)] == "R"]


i = 0
c = "AAA"
while c != "ZZZ":
    c = next(c, i)
    i += 1

print("Part 1:", i)

p2 = 1
for c, *_ in path:
    if c[-1] != "A":
        continue
    i = 0
    while True:
        if c[-1] == "Z":
            break
        c = next(c, i)
        i += 1
    p2 = lcm(p2, i)

print("Part 2:", p2)
