from aoc import *
import re
from math import prod

data: str = read(3)

# Part 1:
# sum(prod(map(int, m)) for m in re.findall(r"mul\((\d+),(\d+)\)", data))

p1 = p2 = 0
enabled = True

for m in re.finditer(r"mul\((\d+),(\d+)\)|do(?:n't)?\(\)", data):
    s = m.group()
    if s[0] == "m":
        t = prod(map(int, m.groups()))
        p1 += t
        p2 += t * enabled
    else:
        enabled = s[2] == "("

print("Part 1:", p1)
print("Part 2:", p2)
