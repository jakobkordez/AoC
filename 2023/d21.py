from aoc import *
from math import ceil

data = read(21, ["\n", list])

H, W = len(data), len(data[0])

start = None
for y in range(H):
    for x in range(W):
        if data[y][x] == "S":
            start = (x, y)
            break
    if start:
        break


def bfs(steps, nbrs):
    st = set([start])

    seen = [set(), set()]
    for i in range(steps):
        ns = set()
        for x, y in st:
            for t in nbrs(x, y):
                if t not in seen[i % 2]:
                    seen[i % 2].add(t)
                    ns.add(t)
        st = ns
    return len(seen[(steps - 1) % 2])


def nbrs1(x, y):
    for dx, dy in FOUR_NEIGHBOURS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and data[ny][nx] != "#":
            yield (nx, ny)


print("Part 1:", bfs(64, nbrs1))


def nbrs2(x, y, data=data, H=H, W=W):
    for dx, dy in FOUR_NEIGHBOURS:
        nx, ny = x + dx, y + dy
        if data[ny % H][nx % W] != "#":
            yield (nx, ny)


mod = 26501365 % H

a = bfs(mod, nbrs2)
b = bfs(mod + H, nbrs2)
c = bfs(mod + H * 2, nbrs2)

fd1 = b - a
fd2 = c - b
sd = fd2 - fd1

A = sd // 2
B = fd1 - 3 * A
C = a - B - A

n = ceil(26501365 / H)
print("Part 2:", A * n**2 + B * n + C)
