from aoc import *
from functools import cache

data = read(21, ["\n"])


def getPos1(c):
    t = "789456123 0A".index(c)
    return (t % 3, t // 3)


def validate(x, y, dx, dy, xx, yy):
    if (x == xx and y + dy == yy) or (x + dx == xx and y == yy):
        return False
    return True


def solve1(code):
    ret = [""]
    x, y = 2, 3
    for c in code:
        tx, ty = getPos1(c)
        dx, dy = tx - x, ty - y
        rx = (">" * dx) if dx > 0 else ("<" * (-dx))
        ry = ("v" * dy) if dy > 0 else ("^" * (-dy))
        nr = []
        if validate(x, y, dx, 0, 0, 3):
            nr.extend(f"{e}{rx}{ry}A" for e in ret)
        if dx != 0 and dy != 0 and validate(x, y, 0, dy, 0, 3):
            nr.extend(f"{e}{ry}{rx}A" for e in ret)
        ret = nr
        x, y = tx, ty
    return ret


def getPos2(c):
    t = " ^A<v>".index(c)
    return (t % 3, t // 3)


@cache
def solve2(code, d):
    if d == 0:
        return len(code)
    ret = 0
    x, y = 2, 0
    for c in code:
        tx, ty = getPos2(c)
        dx, dy = tx - x, ty - y
        rx = (">" * dx) if dx > 0 else ("<" * (-dx))
        ry = ("v" * dy) if dy > 0 else ("^" * (-dy))
        nr = []
        if validate(x, y, dx, 0, 0, 0):
            nr.append(f"{rx}{ry}A")
        if dx != 0 and dy != 0 and validate(x, y, 0, dy, 0, 0):
            nr.append(f"{ry}{rx}A")
        ret += min(solve2(e, d - 1) for e in nr)
        x, y = tx, ty
    return ret


def solve(d):
    result = 0
    for e in data:
        r = min(solve2(p, d) for p in solve1(e))
        result += r * int(e[:-1])
    return result


print("Part 1:", solve(2))
print("Part 2:", solve(25))
