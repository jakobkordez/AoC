from aoc import *
from itertools import cycle, islice

W = 7

jets = read('i17')

field = [['.'] * W for _ in range(5000)]

# Bottom-up
shapes = [
    ['####'],
    ['.#.', '###', '.#.'],
    ['###', '..#', '..#'],
    [*'####'],
    ['##', '##']
]

di = 0

maxy = 0
for shape in islice(cycle(shapes), 2022):
    y = maxy + 3
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
    maxy = max(maxy, y + shapeh)

print('Part 1:', maxy)
