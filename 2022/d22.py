from aoc import *
import re

field, instr = read('i22', ['\n\n'])

field = [*map(list, field.split('\n'))]

countMoves = [*map(int, re.findall(r'\d+', instr))]
turnMoves = re.findall(r'\D+', instr)


def wrapFlat(x, y, dx, dy):
    while 0 <= y-dy < len(field) and \
            0 <= x-dx < len(field[y-dy]) and \
            field[y-dy][x-dx] != ' ':
        y -= dy
        x -= dx
    return x, y, dx, dy


def wrapCube(x, y, dx, dy):
    B = 50
    c = x // B
    r = y // B
    match (c, r, dx, dy):
        case (0, 1, -1, 0):
            return y % B, 2*B, 0, 1
        case (0, 1, 0, -1):
            return B, x % B + B, 1, 0
        case (2, 1, 1, 0):
            return y % B + 2*B, B-1, 0, -1
        case (2, 1, 0, 1):
            return 2*B-1, x % B + B, -1, 0
        case (1, 3, 1, 0):
            return y % B + B, 3*B-1, 0, -1
        case (1, 3, 0, 1):
            return B-1, x % B + 3*B, -1, 0
        case (0, 4, 0, 1):
            return x + 2*B, 0, 0, 1
        case (2, -1, 0, -1):
            return x - 2*B, 4*B-1, 0, -1
        case (2, 2, 1, 0):
            return 3*B - 1, B - 1 - y % B, -1, 0
        case (3, 0, 1, 0):
            return 2*B - 1, 3*B - 1-y % B, -1, 0
        case (-1, 2, -1, 0):
            return B, B - 1 - y % B, 1, 0
        case (0, 0, -1, 0):
            return 0, 3*B - 1 - y % B, 1, 0
        case (-1, 3, -1, 0):
            return B + y % B, 0, 0, 1
        case (1, -1, 0, -1):
            return 0, 3*B + x % B, 1, 0
    raise Exception(f'Invalid: {c}, {r}, {dx}, {dy}')


def toRot(dx, dy):
    match (dx, dy):
        case (1, 0): return 0
        case (0, 1): return 1
        case (-1, 0): return 2
        case (0, -1): return 3


def solve(wrap):
    x = field[0].index('.')
    y = 0

    dx = 1
    dy = 0
    for i in range(len(countMoves) + len(turnMoves)):
        if i % 2:
            match turnMoves[i // 2]:
                case 'L': dx, dy = dy, -dx
                case 'R': dx, dy = -dy, dx
        else:
            for _ in range(countMoves[i // 2]):
                nx, ny = x + dx, y + dy
                ndx, ndy = dx, dy
                if ny >= len(field) or ny < 0 or nx >= len(field[ny]) or nx < 0 or field[ny][nx] == ' ':
                    # Out of bounds
                    nx, ny, ndx, ndy = wrap(nx, ny, dx, dy)
                if field[ny][nx] == '#':
                    # Wall
                    break
                x, y, dx, dy = nx, ny, ndx, ndy

    return 1000 * (y+1) + 4 * (x+1) + toRot(dx, dy)


print('Part 1:', solve(wrapFlat))
print('Part 2:', solve(wrapCube))
