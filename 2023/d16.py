from aoc import *

data = read(16, ["\n", list])

H, W = len(data), len(data[0])


def go(x, y, dx, dy, ener: list[list], seen: set, data=data):
    while True:
        if x < 0 or x >= W or y < 0 or y >= H:
            return
        if (x, y, dx, dy) in seen:
            return
        seen.add((x, y, dx, dy))
        ener[y][x] = True
        if dx != 0 and data[y][x] == "|":
            go(x, y + 1, 0, 1, ener, seen)
            go(x, y - 1, 0, -1, ener, seen)
            return
        if dy != 0 and data[y][x] == "-":
            go(x + 1, y, 1, 0, ener, seen)
            go(x - 1, y, -1, 0, ener, seen)
            return
        if data[y][x] == "\\":
            dx, dy = dy, dx
        elif data[y][x] == "/":
            dx, dy = -dy, -dx
        x += dx
        y += dy


def solve(x, y, dx, dy):
    ener = [[False] * W for _ in range(H)]
    seen = set()
    go(x, y, dx, dy, ener, seen)
    return sum(sum(row) for row in ener)


print("Part 1:", solve(0, 0, 1, 0))


mx = 0

for y in range(W):
    mx = max(mx, solve(0, y, 1, 0))
    mx = max(mx, solve(W - 1, y, -1, 0))

for x in range(H):
    mx = max(mx, solve(x, 0, 0, 1))
    mx = max(mx, solve(x, H - 1, 0, -1))

print("Part 2:", mx)
