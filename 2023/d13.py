from aoc import *

data = read(13, ["\n\n", "\n"], list)

MX = 0


def _solve(data):
    H, W = len(data), len(data[0])
    for y in range(1, H):
        d = 0
        for i in range(min(H - y, y)):
            for x in range(W):
                if data[y - i - 1][x] != data[y + i][x]:
                    d += 1
                    if d > MX:
                        break
            else:
                continue
            break
        if d == MX:
            return y
    return 0


def solve(data):
    ys = _solve(data)
    if ys != 0:
        return ys * 100
    return _solve([*zip(*data)])


print("Part 1:", sum(map(solve, data)))

MX = 1
print("Part 2:", sum(map(solve, data)))
