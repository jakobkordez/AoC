from aoc import *

data = read(18, ["\n", " "])


def solve(data):
    x = y = 0
    p = []
    obr = 0
    for d, c in data:
        obr += c
        if d == 0:
            x += c
        elif d == 1:
            y += c
        elif d == 2:
            x -= c
        elif d == 3:
            y -= c
        p.append((x, y))

    a = 0
    for (x1, y1), (x2, y2) in zip(p, roll(p, 1)):
        a += x1 * y2 - x2 * y1

    return (abs(a) + obr) // 2 + 1


print("Part 1:", solve(("RDLU".find(d), int(c)) for d, c, _ in data))
print("Part 2:", solve((int(h[7]), int(h[2:7], 16)) for _, _, h in data))
