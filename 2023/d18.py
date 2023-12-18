from aoc import *

data = read(18, ["\n", " "])


def solve(data):
    x = y = 0
    a = o = 0
    for d, c in data:
        o += c
        nx, ny = x, y
        if d == 0:
            nx += c
        elif d == 1:
            ny += c
        elif d == 2:
            nx -= c
        elif d == 3:
            ny -= c
        a += x * ny - nx * y
        x, y = nx, ny

    return (abs(a) + o) // 2 + 1


print("Part 1:", solve(("RDLU".find(d), int(c)) for d, c, _ in data))
print("Part 2:", solve((int(h[7]), int(h[2:7], 16)) for _, _, h in data))
