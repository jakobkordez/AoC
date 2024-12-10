from aoc import *
from functools import cache

data = read(10, ["\n", list, int])
H, W = len(data), len(data[0])


@cache
def go(x, y):
    h = data[y][x]
    if h == 9:
        return {(x, y)}, 1
    st = set()
    sr = 0
    for dx, dy in FOUR_NEIGHBOURS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and data[ny][nx] == h + 1:
            s1, s2 = go(nx, ny)
            st.update(s1)
            sr += s2
    return st, sr


p1 = p2 = 0
for y in range(H):
    for x in range(W):
        if data[y][x] != 0:
            continue
        s1, s2 = go(x, y)
        p1 += len(s1)
        p2 += s2

print("Part 1:", p1)
print("Part 2:", p2)
