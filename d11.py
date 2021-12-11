import numpy as np

with open('i11.txt') as file:
    d = np.array([list(a.strip()) for a in file.readlines()], dtype=np.int32)

p1 = 0
p2 = 0
while not np.all(d == 0):
    d += 1
    p2 += 1
    fl = np.zeros_like(d, dtype=np.bool8)
    while True:
        nfl = np.logical_and(d > 9, np.logical_not(fl))
        if not nfl.any():
            break
        fl |= nfl
        for y, x in np.argwhere(nfl):
            d[max(0, y-1):y+2, max(0, x-1):x+2] += 1
    p1 += np.sum(fl)
    d[np.nonzero(fl)] = 0
    if p2 == 100:
        print(p1)

print(p2)
