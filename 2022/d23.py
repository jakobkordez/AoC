from aoc import *
from collections import Counter

p = read('i23', ['\n', list])

elves = []
for y in range(len(p)):
    for x in range(len(p[y])):
        if p[y][x] == '#':
            elves.append((x, y))

R3 = (-1, 0, 1)
checks = [(R3, -1), (R3, 1), (-1, R3), (1, R3)]

r = 0
while True:
    elvesSet = set(elves)
    newElves = []
    for x, y in elves:
        if all((x+dx, y+dy) not in elvesSet for dx, dy in EIGHT_NEIGHBOURS):
            newElves.append((x, y))
        else:
            for i in range(4):
                xt, yt = checks[(r + i) % 4]
                if type(xt) == int:
                    if all((x+xt, y+dy) not in elvesSet for dy in yt):
                        newElves.append((x+xt, y))
                        break
                else:
                    if all((x+dx, y+yt) not in elvesSet for dx in xt):
                        newElves.append((x, y+yt))
                        break
            else:
                newElves.append((x, y))

    newElves2 = []
    cnt = Counter(newElves)
    for op, np in zip(elves, newElves):
        if cnt[np] > 1:
            newElves2.append(op)
        else:
            newElves2.append(np)

    elves = newElves2
    r += 1

    if elvesSet == set(elves):
        print('Part 2:', r)
        break
    if r == 10:
        mnx = mxx = elves[0][0]
        mny = mxy = elves[0][1]
        for x, y in elves:
            mxx = max(mxx, x)
            mnx = min(mnx, x)
            mxy = max(mxy, y)
            mny = min(mny, y)

        print('Part 1:', (mxx-mnx+1) * (mxy-mny+1) - len(elves))
