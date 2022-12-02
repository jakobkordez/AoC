import numpy as np

with open('i22.txt') as f:
    data = []
    for l in f.read().strip().split('\n'):
        state, pos = l.split()
        state = state == 'on'
        pos = [[int(e)+50+i for i, e in enumerate(x[2:].split('..'))]
               for x in pos.split(',')]
        data += [(state, pos)]


a = np.zeros((101, 101, 101), dtype=np.int32)

for state, pos in data[:20]:
    x, y, z = pos
    a[z[0]:z[1], y[0]:y[1], x[0]:x[1]] = state

print('Part 1:', np.sum(a))
