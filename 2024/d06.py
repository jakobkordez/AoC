from aoc import *

data = read(6, ["\n", list])

h, w = len(data), len(data[0])

for y in range(h):
    for x in range(w):
        if data[y][x] == "^":
            break
    else:
        continue
    break

sx, sy = x, y
dx, dy = 0, -1

p1 = 1
while 0 <= x + dx < w and 0 <= y + dy < h:
    if data[y + dy][x + dx] == "#":
        dx, dy = -dy, dx  # Turn right
        continue
    x, y = x + dx, y + dy
    if data[y][x] == ".":
        p1 += 1
        data[y][x] = "X"

print("Part 1:", p1)

p2 = 0
for oy in range(h):
    for ox in range(w):
        if data[oy][ox] != "X":
            continue
        data[oy][ox] = "#"
        cache = set()
        x, y, dx, dy = sx, sy, 0, -1
        while 0 <= x + dx < w and 0 <= y + dy < h:
            if data[y + dy][x + dx] == "#":
                dx, dy = -dy, dx  # Turn right
                continue
            x, y = x + dx, y + dy
            if (x, y, dx, dy) in cache:
                p2 += 1
                break
            cache.add((x, y, dx, dy))
        data[oy][ox] = "X"

print("Part 2:", p2)
