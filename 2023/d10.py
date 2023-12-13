from aoc import *
from collections import deque

p = read(10, ["\n", list])

H, W = len(p), len(p[0])

q = deque()

for y in range(H):
    for x in range(W):
        if p[y][x] == "S":
            q.append((x, y, 0))
            break
    if q:
        break

done = [[False] * W for _ in range(H)]

p1 = 0
while q:
    x, y, i = q.popleft()

    if done[y][x]:
        continue
    done[y][x] = True

    c = p[y][x]
    wc = 0
    if c in "S|F7" and y < H - 1 and p[y + 1][x] in "|LJ":
        q.append((x, y + 1, i + 1))
        wc += 1
    if c in "S|LJ" and y > 0 and p[y - 1][x] in "|7F":
        q.append((x, y - 1, i + 1))
        wc += 2
    if c in "S-FL" and x < W - 1 and p[y][x + 1] in "-J7":
        q.append((x + 1, y, i + 1))
        wc += 4
    if c in "S-J7" and x > 0 and p[y][x - 1] in "-LF":
        q.append((x - 1, y, i + 1))
        wc += 8
    if c == "S":
        p[y][x] = "   | FL  7J -"[wc]
    p1 = i

print("Part 1:", p1)


p2 = 0
for y in range(H):
    c = 0
    for x in range(W):
        if not done[y][x]:
            if c % 2 == 1:
                p2 += 1
        else:
            if p[y][x] in "|FL":
                last = p[y][x]
                c += 1
            elif p[y][x] == "7" and last == "F":
                c += 1
            elif p[y][x] == "J" and last == "L":
                c += 1


print("Part 2:", p2)
