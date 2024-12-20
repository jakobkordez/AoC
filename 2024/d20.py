from aoc import *

data = read(20, ["\n", list])

H, W = len(data), len(data[0])

for y in range(H):
    for x in range(W):
        if data[y][x] == "S":
            break
    else:
        continue
    break

p = [[-1] * W for _ in range(H)]

c = 0
while data[y][x] != "E":
    p[y][x] = c
    c += 1
    for dx, dy in FOUR_NEIGHBOURS:
        if data[y + dy][x + dx] != "#" and p[y + dy][x + dx] == -1:
            y += dy
            x += dx
            break
p[y][x] = c


def solve(n):
    flower = [[(1, 0), (0, 1), (0, -1), (-1, 0)]]
    for i in range(2, n + 1):
        l = flower[-1]
        nxt = (
            [(x + 1, y) for x, y in l[: len(l) // 2 + 1]]
            + [(0, i), (0, -i)]
            + [(x - 1, y) for x, y in l[len(l) // 2 - 1 :]]
        )
        flower.append(nxt)

    flower = [e for s in flower for e in s]

    result = 0
    for y in range(H):
        for x in range(W):
            if data[y][x] == "#":
                continue
            for dx, dy in flower:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < W
                    and 0 <= ny < H
                    and data[ny][nx] != "#"
                    and p[ny][nx] - p[y][x] - abs(dy) - abs(dx) >= 100
                ):
                    result += 1
    return result


print("Part 1:", solve(2))
print("Part 2:", solve(20))
