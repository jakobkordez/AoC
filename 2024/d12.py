from aoc import *
import numpy as np

data = np.pad(read(12, ["\n", list]), (1, 1), "constant", constant_values=".")
h, w = data.shape

p1 = 0
handled = set()
for sy in range(1, h - 1):
    for sx in range(1, w - 1):
        if (sx, sy) in handled:
            continue
        a = p = 0
        q = [(sx, sy)]
        handled.add((sx, sy))
        while q:
            x, y = q.pop()
            a += 1
            for dx, dy in FOUR_NEIGHBOURS:
                nx, ny = x + dx, y + dy
                if data[ny, nx] != data[y, x]:
                    p += 1
                if data[ny, nx] == data[y, x] and (nx, ny) not in handled:
                    q.append((nx, ny))
                    handled.add((nx, ny))
        p1 += a * p

print("Part 1:", p1)
