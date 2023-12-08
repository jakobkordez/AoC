from aoc import *
import re
from math import lcm
from itertools import cycle

((instr,),), path = read(8, ["\n\n", "\n", re.compile(r"\w+")])


d = {}
for s, l, r in path:
    d[s] = (l, r)


instrCyc = cycle(x == "R" for x in instr)
i = 0
c = "AAA"
while c != "ZZZ":
    c = d[c][next(instrCyc)]
    i += 1

print("Part 1:", i)


p2 = 1
for c, *_ in path:
    if c[-1] != "A":
        continue

    instrCyc = cycle(x == "R" for x in instr)
    i = 0
    while c[-1] != "Z":
        c = d[c][next(instrCyc)]
        i += 1
    p2 = lcm(p2, i)

print("Part 2:", p2)
