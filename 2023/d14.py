from aoc import *


def parse(r):
    return [0 if c == "O" else (1 if c == "#" else 2) for c in r]


data = read(14, ["\n", parse])

H, W = len(data), len(data[0])


def roll(x, y, dx, dy, data=data, H=H, W=W):
    jx, jy = x, y
    mf = max if dx + dy > 0 else min
    while 0 <= y and y < H and 0 <= x and x < W:
        if data[y][x] == 2:
            jx = mf(jx, x + dx)
            jy = mf(jy, y + dy)
            while 0 <= jy and jy < H and 0 <= jx and jx < W:
                t = data[jy][jx]
                if t == 1:
                    x, y = jx, jy
                    break
                if t == 0:
                    data[jy][jx] = data[y][x]
                    data[y][x] = t
                    break
                jx += dx
                jy += dy
        x += dx
        y += dy


def north():
    for x in range(W):
        roll(x, 0, 0, 1)


def cycle():
    north()
    for y in range(H):
        roll(0, y, 1, 0)
    for x in range(W):
        roll(x, H - 1, 0, -1)
    for y in range(H):
        roll(W - 1, y, -1, 0)


def calc():
    return sum(data[y].count(0) * (H - y) for y in range(H))


north()
print("Part 1:", calc())


history = set()
h = []
ch = []
while True:
    s = str(data)
    if s in history:
        break
    history.add(s)
    h.append(s)
    ch.append(calc())
    cycle()

offset = h.index(s)
repeat = len(history) - offset
print("Part 2:", ch[((1000000000 - offset) % repeat) + offset])
