from aoc import *
import re
from math import lcm

((instr,),), path = read(8, ["\n\n", "\n", re.compile(r"\w+")])


d = {}
for s, l, r in path:
    d[s] = (l, r)


i = 0
c = "AAA"
while c != "ZZZ":
    c = d[c][instr[i % len(instr)] == "R"]
    i += 1

print("Part 1:", i)

p2 = 1
for cc in [k for k in d.keys() if k[-1] == "A"]:
    i = 0
    while True:
        if cc[-1] == "Z":
            break
        cc = d[cc][instr[i % len(instr)] == "R"]
        i += 1
    p2 = lcm(p2, i)

print("Part 2:", p2)
