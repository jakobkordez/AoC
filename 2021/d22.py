import numpy as np

with open('i22.txt') as f:
    data = []
    for l in f.read().strip().split('\n'):
        state, pos = l.split()
        state = state == 'on'
        pos = [[int(e)+50+i for i, e in enumerate(x[2:].split('..'))]
               for x in pos.split(',')]
        data += [(state, pos)]


def overlap1d(a, b):
    left = max(a[0], b[0])
    right = min(a[1], b[1])
    return left, right, max(0, right - left)


def overlap3d(a, b):
    xl, xr, xo = overlap1d(a[0], b[0])
    yl, yr, yo = overlap1d(a[1], b[1])
    zl, zr, zo = overlap1d(a[2], b[2])
    return (xl, xr), (yl, yr), (zl, zr), xo*yo*zo


d = []


def calcSol():
    s = 0
    for x, y, z in d:
        s += (x[1]-x[0]) * (y[1]-y[0]) * (z[1]-z[0])
    return s


for it, (state, pos) in enumerate(data):
    i = 0
    c = len(d)
    while i < c:
        p = d[i]
        x, y, z, o = overlap3d(pos, p)
        if o:
            (xol, xor), (yol, yor), (zol, zor) = x, y, z
            (xl, xr), (yl, yr), (zl, zr) = p
            if xl < xol:
                d += [((xl, xol), (yl, yr), (zl, zr))]
            if xor < xr:
                d += [((xor, xr), (yl, yr), (zl, zr))]
            if yl < yol:
                d += [((xol, xor), (yl, yol), (zl, zr))]
            if yor < yr:
                d += [((xol, xor), (yor, yr), (zl, zr))]
            if zl < zol:
                d += [((xol, xor), (yol, yor), (zl, zol))]
            if zor < zr:
                d += [((xol, xor), (yol, yor), (zor, zr))]
            c -= 1
            d.pop(i)
        else:
            i += 1
    if state:
        d += [pos]
    if it == 19:
        print('Part 1:', calcSol())

print('Part 2:', calcSol())
