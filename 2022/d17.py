from aoc import *

W = 7

jets = read('i17')

field = [['.'] * W for _ in range(10000)]

# Bottom-up
shapes = [
    ['####'],
    ['.#.', '###', '.#.'],
    ['###', '..#', '..#'],
    [*'####'],
    ['##', '##']
]

si = di = 0


def place(shape, y):
    global di
    x = 2
    shapeh, shapew = len(shape), len(shape[0])
    while y >= 0:
        # Jets
        jetd = jets[di % len(jets)]
        di += 1
        dx = 0
        if jetd == '>' and x < W - shapew:
            dx = 1
        elif jetd == '<' and x > 0:
            dx = -1
        x += dx
        # Check collision
        colides = False
        for yy in range(shapeh):
            for xx in range(shapew):
                if shape[yy][xx] == '#' and field[y + yy][x + xx] == '#':
                    colides = True
                    break
            if colides:
                break
        if colides:
            x -= dx
        y -= 1
        # Check collision
        colides = y < 0
        for yy in range(shapeh):
            for xx in range(shapew):
                if shape[yy][xx] == '#' and field[y + yy][x + xx] == '#':
                    colides = True
                    break
            if colides:
                break
        if colides:
            y += 1
            break
    # Place
    for yy in range(shapeh):
        for xx in range(shapew):
            if shape[yy][xx] == '#':
                field[y + yy][x + xx] = '#'
    return y


dct = {}

placed = maxy = 0
while True:
    shape = shapes[si % len(shapes)]
    si += 1

    y = place(shape, maxy + 3)

    maxy = max(maxy, y + len(shape))
    placed += 1

    if placed == 2022:
        print('Part 1:', maxy)

    key = (di % len(jets), si % len(shapes))
    if key in dct and placed > 3000:
        break
    dct[key] = placed, maxy

TARGET = 1000000000000
oldp, oldy = dct[key]
segBlocks = placed - oldp
segHeight = maxy - oldy
segCount = (TARGET - placed) // segBlocks
placed += segCount * segBlocks

while placed < TARGET:
    shape = shapes[si % len(shapes)]
    si += 1

    y = place(shape, maxy + 3)

    maxy = max(maxy, y + len(shape))
    placed += 1

print('Part 2:', maxy + segHeight * segCount)
