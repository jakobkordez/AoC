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


p1 = None
p2 = 0
y = 1
while y != 0:
    x, y = 500, 0
    while y <= mxy:
        if not field[y+1][x]:
            y += 1
        elif not field[y+1][x-1]:
            x -= 1
            y += 1
        elif not field[y+1][x+1]:
            x += 1
            y += 1
        else:
            break
    else:
        if p1 == None:
            p1 = p2
    field[y][x] = True
    p2 += 1


print('Part 1:', p1)
print('Part 2:', p2)
