from aoc import *

data = read(11, ["\n"], list)

H, W = len(data), len(data[0])

stars = []

col = [1] * W
row = [1] * H
for y in range(H):
    for x in range(W):
        if data[y][x] == "#":
            col[x] = row[y] = 0
            stars.append((x, y))

col = rollSum(col)
row = rollSum(row)

N = len(stars)

p1 = p2 = 0
for i in range(N - 1):
    x1, y1 = stars[i]
    for j in range(i + 1, N):
        x2, y2 = stars[j]

        dxy = abs(x1 - x2) + abs(y1 - y2)
        sxy = abs(col[x2] - col[x1]) + abs(row[y2] - row[y1])
        p1 += dxy + sxy
        p2 += dxy + sxy * 999999


print("Part 1:", p1)
print("Part 2:", p2)
