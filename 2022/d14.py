from aoc import *

data = read('i14', ['\n', ' -> ', ','], int)

field = [[False]*1000 for _ in range(1000)]
mxy = 0

for seg in data:
    for (x1, y1), (x2, y2) in zip(seg, seg[1:]):
        if x1 > x2:
            x1, x2 = x2, x1
        elif y1 > y2:
            y1, y2 = y2, y1
        mxy = max(mxy, y2)

        if x1 == x2:
            for y in range(y1, y2+1):
                field[y][x1] = True
        else:
            for x in range(x1, x2+1):
                field[y1][x] = True


def solve(x, y, p1):
    if y > mxy + 1:
        return p1, 0
    if field[y][x]:
        return False, 0

    r = 0
    for dx in [0, -1, 1]:
        ex, tr = solve(x+dx, y+1, p1)
        r += tr
        if ex:
            return True, r

    field[y][x] = True
    return False, r + 1


s1 = solve(500, 0, True)[1]
s2 = solve(500, 0, False)[1]

print('Part 1:', s1)
print('Part 2:', s1 + s2)
