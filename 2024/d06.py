from aoc import *
from bisect import insort, bisect

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

rows = [[] for _ in range(h)]
cols = [[] for _ in range(w)]
for y in range(h):
    for x in range(w):
        if data[y][x] == "#":
            rows[y].append(x)
            cols[x].append(y)


p2 = 0
for oy in range(h):
    for ox in range(w):
        if data[oy][ox] != "X":
            continue

        insort(rows[oy], ox)
        insort(cols[ox], oy)

        cache = set()
        x, y, dx, dy = sx, sy, 0, -1

        while True:
            if dx != 0:
                i = bisect(rows[y], x)
                if dx > 0 and i < len(rows[y]):
                    x = rows[y][i] - 1
                elif dx < 0 and i > 0:
                    x = rows[y][i - 1] + 1
                else:
                    break
            else:
                i = bisect(cols[x], y)
                if dy > 0 and i < len(cols[x]):
                    y = cols[x][i] - 1
                elif dy < 0 and i > 0:
                    y = cols[x][i - 1] + 1
                else:
                    break
            dx, dy = -dy, dx  # Turn right
            if (x, y, dx, dy) in cache:
                p2 += 1
                break
            cache.add((x, y, dx, dy))

        rows[oy].remove(ox)
        cols[ox].remove(oy)

print("Part 2:", p2)
