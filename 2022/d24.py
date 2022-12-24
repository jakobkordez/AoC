from aoc import *

field = read('i24', ['\n', list])
H = len(field)
W = len(field[0])

MOVES = (*FOUR_NEIGHBOURS, (0, 0))


def stepField():
    global field
    newField = [['']*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            for e in field[y][x]:
                tx, ty = x, y
                match e:
                    case '.': continue
                    case '>': tx = 1 if x == W-2 else x+1
                    case '<': tx = W-2 if x == 1 else x-1
                    case '^': ty = H-2 if y == 1 else y-1
                    case 'v': ty = 1 if y == H-2 else y+1
                newField[ty][tx] += e
    field = newField


def solve(start, end_y):
    q = [start]
    it = 0

    while True:
        it += 1
        stepField()
        newQ = set()
        for x, y in q:
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if field[ny % H][nx % W] == '':
                    if ny == end_y:
                        return it
                    newQ.add((nx, ny))
        q = newQ


p1 = solve((1, 0), H-1)
print('Part 1:', p1)

p2 = p1 + solve((W-2, H-1), 0) + solve((1, 0), H-1)
print('Part 2:', p2)
