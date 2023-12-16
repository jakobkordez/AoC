from aoc import *

data = read(11, ["\n", list])

H, W = len(data), len(data[0])

col = [True] * W
row = [True] * H
for y in range(H):
    for x in range(W):
        if data[y][x] == "#":
            col[x] = row[y] = False


def solve(mult):
    t = stars = 0
    colCount = [0] * W

    solution = 0
    startR = 0
    for y in range(H):
        if row[y]:
            t += stars * mult
            continue

        l = lstars = 0
        starsInRow = 0
        r = startR
        rstars = stars
        trux = 0
        for x in range(W):
            colx = mult if col[x] else 1
            trux += colx

            r -= rstars * colx
            rstars -= colCount[x]
            if data[y][x] == "#":
                starsInRow += 1
                colCount[x] += 1
                solution += t + l + r
                startR += trux
            lstars += colCount[x]
            l += lstars * colx

        stars += starsInRow
        t += stars

    return solution


print("Part 1:", solve(2))
print("Part 2:", solve(1000000))
