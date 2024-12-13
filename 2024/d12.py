from aoc import *
import numpy as np

data = np.pad(read(12, ["\n", list]), (1, 1), "constant", constant_values=".")
h, w = data.shape

pp = np.zeros((h, w))

p1 = p2 = 0
rc = 0
for sy in range(1, h - 1):
    for sx in range(1, w - 1):
        if pp[sy, sx] > 0:
            continue
        a = p = c = 0
        q = [(sx, sy)]
        rc += 1
        pp[sy, sx] = rc
        while q:
            x, y = q.pop()
            a += 1
            for dx, dy in FOUR_NEIGHBOURS:
                nx, ny = x + dx, y + dy
                rx, ry = x - dy, y + dx
                cx, cy = x + dx - dy, y + dy + dx
                if data[ny, nx] != data[y, x]:
                    p += 1
                    if data[ry, rx] != data[y, x]:
                        c += 1
                else:
                    if pp[ny, nx] == 0:
                        q.append((nx, ny))
                        pp[ny, nx] = rc
                    if data[ry, rx] == data[y, x] and data[cy, cx] != data[y, x]:
                        c += 1

        p1 += a * p
        p2 += a * c

print("Part 1:", p1)
print("Part 2:", p2)
