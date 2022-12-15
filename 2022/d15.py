from aoc import *
import re

sensors = read('i15', ['\n', re.compile(r'-?\d+')], int)
sensors.sort()

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


def solve(y):
    r = []
    for sx, sy, bx, by in sensors:
        mdist = abs(sx - bx) + abs(sy - by) - abs(sy - y)
        if mdist > 0:
            r += [(sx - mdist, sx + mdist + 1)]

    r.sort()
    mxr = r[0][1]
    for left, right in r[1:]:
        if left > mxr:
            return left - 1,  y
        mxr = max(mxr, right)


for y in range(M4, 0, -1):
    s2 = solve(y)
    if s2:
        print('Part 2:', s2[1] + s2[0]*M4)
        break
