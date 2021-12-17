import numpy as np

with open('i15.txt') as file:
    data = np.array([list(map(int, list(r.strip())))
                    for r in file.readlines()])


def go(data):
    mn = np.zeros_like(data) + 999999999
    h, w = mn.shape

    mn[0, 0] = 0
    rec = {(0, 1), (1, 0)}

    while len(rec) != 0:
        y, x = rec.pop()
        p = 999999999
        if y != 0:
            p = min(p, mn[y-1, x])
        if x != 0:
            p = min(p, mn[y, x-1])
        if y + 1 < h:
            p = min(p, mn[y+1, x])
        if x + 1 < w:
            p = min(p, mn[y, x+1])
        p += data[y, x]
        if p < mn[y, x]:
            mn[y, x] = p
            if y != 0:
                rec.add((y-1, x))
            if x != 0:
                rec.add((y, x-1))
            if y + 1 < h:
                rec.add((y+1, x))
            if x + 1 < w:
                rec.add((y, x+1))

    return mn[-1, -1]


print('Part 1:', go(data))

h, w = data.shape
data = np.tile(data, (5, 5))
for y in range(len(data)):
    for x in range(len(data[y])):
        data[y, x] = ((data[y, x] + y//h + x//w - 1) % 9) + 1

print('Part 2:', go(data))
