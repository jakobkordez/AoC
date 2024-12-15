from aoc import *

dm = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
big = {"@": "@.", "#": "##", "O": "[]", ".": ".."}

p_original, moves = read(15, ["\n\n", "\n"])
moves = [dm[m] for m in "".join(moves)]


def go(p, x, y, dx, dy, move=False):
    if p[y + dy][x + dx] == "#":
        return False
    if p[y + dy][x + dx] == ".":
        if move:
            p[y][x], p[y + dy][x + dx] = p[y + dy][x + dx], p[y][x]
        return True
    if dy != 0 and p[y + dy][x + dx] != "O":
        ddx = -1 if p[y + dy][x] == "]" else 1
        if not (go(p, x, y + dy, 0, dy, move) and go(p, x + ddx, y + dy, 0, dy, move)):
            return False
        if move:
            p[y][x], p[y + dy][x] = p[y + dy][x], p[y][x]
        return True
    if not go(p, x + dx, y + dy, dx, dy, move):
        return False
    if move:
        p[y][x], p[y + dy][x + dx] = p[y + dy][x + dx], p[y][x]
    return True


def solve(p):
    H, W = len(p), len(p[0])

    for y in range(H):
        for x in range(W):
            if p[y][x] == "@":
                p[y][x] = "."
                break
        else:
            continue
        break

    for dy, dx in moves:
        if not go(p, x, y, dx, dy, False):
            continue
        go(p, x, y, dx, dy, True)
        x += dx
        y += dy

    return sum(y * 100 + x for y in range(H) for x in range(W) if p[y][x] in "O[")


print("Part 1:", solve(list(map(list, p_original))))
print("Part 2:", solve([list("".join(big[a] for a in row)) for row in p_original]))
