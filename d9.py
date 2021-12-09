import numpy as np

with open('i9.txt') as file:
    data = np.array([list(a.strip()) for a in file.readlines()], dtype=np.int8)


t = np.pad(data, (1, 1), 'constant', constant_values=9)
h = np.pad(data, (2, 2), 'constant', constant_values=9)

r = np.all([t < h[1:-1, :-2], t < h[1:-1, 2:], t <
           h[:-2, 1:-1], t < h[2:, 1:-1]], axis=0)

print('Part 1:', sum(t[np.nonzero(r)] + 1))


t = np.pad(data, (1, 1), 'constant', constant_values=9) != 9


def rec(y, x):
    if not t[y][x]:
        return 0
    t[y][x] = False
    return 1 + rec(y-1, x) + rec(y+1, x) + rec(y, x-1) + rec(y, x+1)


bas = sorted([rec(y, x) for y, x in np.ndindex(data.shape)])

print('Part 2:', bas[-1]*bas[-2]*bas[-3])
