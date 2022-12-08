from aoc import *

trees = read('i08', ['\n', list], int)

h = len(trees)
w = len(trees[0])


def f(x, y, dx, dy):
    val = trees[y][x]
    nx, ny = x+dx, y+dy

    while 0 <= nx < w and 0 <= ny < h and trees[ny][nx] < val:
        nx += dx
        ny += dy

    p1 = nx < 0 or nx == w or ny < 0 or ny == h
    p2 = abs(x - min(max(0, nx), w-1) + y - min(max(0, ny), h-1))
    return p1, p2


p1 = p2 = 0
for i in range(h):
    for j in range(w):
        t1, s1 = f(j, i, 0, 1)
        t2, s2 = f(j, i, 0, -1)
        t3, s3 = f(j, i, 1, 0)
        t4, s4 = f(j, i, -1, 0)
        p1 += t1 or t2 or t3 or t4
        p2 = max(p2, s1 * s2 * s3 * s4)

print('Part 1:', p1)
print('Part 2:', p2)
