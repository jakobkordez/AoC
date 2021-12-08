import numpy as np

with open('i8.txt') as file:
    d = [[a.split() for a in l.split(' | ')] for l in file.readlines()]


dd = np.bincount([len(oo) for _, o in d for oo in o], minlength=8)
print('Part 1:', sum(dd[[2, 3, 4, 7]]))

sm = 0
for i, o in d:
    i = [set(a) for a in i]
    n = [None] * 10

    n[1], n[7], n[4], *i, n[8] = sorted(i, key=len)

    h = n[8] - n[4]
    n[5], n[2], n[6], n[3], n[9], n[0] = \
        sorted(i, key=lambda x: (x.issuperset(n[1]), len(x), x.issuperset(h)))

    sm += int(''.join([str(n.index(set(a))) for a in o]))

print('Part 2:', sm)
