from aoc import *
import re

symb = re.compile(r"[^\.\d]")
nums = re.compile(r"\d+")

data = read(3, ["\n"])

H = len(data)
W = len(data[0])

p = [list(nums.finditer(l)) for l in data]

p1 = 0
for y in range(H):
    for pp in p[y]:
        s, e = pp.span()
        if any(
            symb.search(data[i], s - 1, e + 1)
            for i in range(max(0, y - 1), min(H, y + 2))
        ):
            p1 += int(pp.group(0))

print("Part 1:", p1)


p2 = 0
for y in range(H):
    for x in range(W):
        if data[y][x] != "*":
            continue
        nrs = []
        for i in range(max(0, y - 1), min(H, y + 2)):
            for g in p[i]:
                s, e = g.span()
                if e >= x and s <= x + 1:
                    nrs.append(int(g.group(0)))
        if len(nrs) == 2:
            p2 += nrs[0] * nrs[1]

print("Part 2:", p2)
