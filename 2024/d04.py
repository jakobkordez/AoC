from aoc import *

data = read(4, ["\n", list])

h, w = len(data), len(data[0])

S = "XMAS"

p1 = 0
for y in range(h):
    for x in range(w):
        if data[y][x] != "X":
            continue
        for dx, dy in EIGHT_NEIGHBOURS:
            fx = x + dx * 3
            fy = y + dy * 3
            if fx < 0 or fx >= w or fy < 0 or fy >= h:
                continue
            for i in range(1, 4):
                if data[y + dy * i][x + dx * i] != S[i]:
                    break
            else:
                p1 += 1

print("Part 1:", p1)

p2 = 0
hs = set(["M", "S"])
for y in range(1, h - 1):
    for x in range(1, w - 1):
        if data[y][x] != "A":
            continue
        p2 += (
            set([data[y - 1][x - 1], data[y + 1][x + 1]]) == hs
            and set([data[y - 1][x + 1], data[y + 1][x - 1]]) == hs
        )


print("Part 2:", p2)
