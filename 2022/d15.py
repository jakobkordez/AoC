from aoc import *
import re

sensors = read('i15', ['\n', re.compile(r'-?\d+')], int)

y = 2_000_000

mn = 10e9
mx = 0
s1 = 0
bcons = set()
for sx, sy, bx, by in sensors:
    s1 -= by == y and (bx, by) not in bcons
    bcons.add((bx, by))
    mdist = abs(sx - bx) + abs(sy - by) - abs(sy - y)
    if mdist > 0:
        mn = min(mn, sx - mdist)
        mx = max(mx, sx + mdist + 1)

print('Part 1:', mx - mn + s1)


M4 = 4_000_000


def get_kn(a, b):
    """ Get line k and n from two points """
    if a > b:
        a, b = b, a
    k = 1 if a[1] < b[1] else -1
    n = a[1] - k*a[0]
    return k, n


lines = set()
for sx, sy, bx, by in sensors:
    mdist = abs(sx - bx) + abs(sy - by)
    top = (sx, sy - mdist - 1)
    rig = (sx + mdist + 1, sy)
    bot = (sx, sy + mdist + 1)
    lef = (sx - mdist - 1, sy)
    lines |= {
        get_kn(top, rig),
        get_kn(rig, bot),
        get_kn(bot, lef),
        get_kn(lef, top)
    }


points = set()
lines = list(lines)
for i, (k1, n1) in enumerate(lines):
    for k2, n2 in lines[i+1:]:
        if k1 == k2:
            continue
        x = (n2 - n1) / (k1 - k2)
        if x != int(x):
            continue
        x = int(x)
        y = k1*x + n1
        if 0 <= x < M4 and 0 <= y < M4:
            points |= {(x, y)}


for x, y in points:
    for sx, sy, bx, by in sensors:
        mdist = abs(sx - bx) + abs(sy - by)
        if abs(sx - x) + abs(sy - y) <= mdist:
            break
    else:
        print('Part 2:', x*M4 + y)
        break
