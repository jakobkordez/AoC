from aoc import *
import re

data = read(4, ["\n", ": ", " | "])

p1 = 0
p2 = [1] * len(data)

for i, (_, (w, m)) in enumerate(data):
    w = set(map(int, re.findall(r"\d+", w)))
    m = set(map(int, re.findall(r"\d+", m)))
    o = w & m

    p1 += int(2 ** (len(o) - 1))
    for j in range(len(o)):
        p2[i + j + 1] += p2[i]

print("Part 1:", p1)
print("Part 2:", sum(p2))
