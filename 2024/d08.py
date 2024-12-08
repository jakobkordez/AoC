from aoc import *
from collections import defaultdict
from itertools import permutations

data = read(8, ["\n", list])
h, w = len(data), len(data[0])

antennas = defaultdict(lambda: [])

for y, row in enumerate(data):
    for x, col in enumerate(row):
        if col != ".":
            antennas[col].append((x, y))

p1 = set()
p2 = set()

for ant in antennas.values():
    for (ax, ay), (bx, by) in permutations(ant, 2):
        p2.add((bx, by))
        dx, dy = bx - ax, by - ay
        x, y = bx + dx, by + dy
        if 0 <= x < w and 0 <= y < h:
            p1.add((x, y))
        while 0 <= x < w and 0 <= y < h:
            p2.add((x, y))
            x += dx
            y += dy

print("Part 1:", len(p1))
print("Part 2:", len(p2))
