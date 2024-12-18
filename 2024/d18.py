from aoc import *
from collections import deque
from bisect import bisect

data = read(18, ["\n", ",", int])
H = W = 71

p = [[len(data)] * W for _ in range(H)]
for i, (x, y) in enumerate(data):
    p[y][x] = i


def solve(lim):
    q = deque([(0, 0, 0)])
    vis = set()
    while q:
        x, y, s = q.popleft()
        if x == W - 1 and y == H - 1:
            return s
        for dx, dy in FOUR_NEIGHBOURS:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < W and 0 <= ny < H and lim <= p[ny][nx] and (nx, ny) not in vis:
                q.append((nx, ny, s + 1))
                vis.add((nx, ny))
    return None


print("Part 1:", solve(1024))

r = binarySearch(1024, len(data), lambda x: solve(x) == None) - 1
print("Part 2:", ",".join(map(str, data[r])))
