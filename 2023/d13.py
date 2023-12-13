from aoc import *


def mapToBits(s: str):
    return int(s.replace(".", "0").replace("#", "1"), 2)


def parse(p: str):
    p = p.split("\n")
    return [*map(mapToBits, p)], [*map(mapToBits, map("".join, zip(*p)))]


data = read(13, ["\n\n", parse])

MX = 0


def _solve(data: list[int]):
    H = len(data)
    for y in range(1, H):
        d = 0
        for i in range(min(H - y, y)):
            d += (data[y - i - 1] ^ data[y + i]).bit_count()
            if d > MX:
                break
        if d == MX:
            return y
    return 0


def solve(data):
    ys = _solve(data[0])
    if ys != 0:
        return ys * 100
    return _solve(data[1])


print("Part 1:", sum(map(solve, data)))

MX = 1
print("Part 2:", sum(map(solve, data)))
