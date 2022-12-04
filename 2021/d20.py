import numpy as np

with open('i20.txt') as f:
    key, mp = f.read().strip().split('\n\n')

key = np.array([int(e == '#') for e in key])

mp = np.array([[int(e == '#') for e in line] for line in mp.split()])

mp = np.pad(mp, 50, 'constant', constant_values=0)

for i in range(50):
    h, w = mp.shape
    t = np.pad(mp, 1, 'constant', constant_values=i % 2)
    ci = 2**8
    r = np.zeros_like(mp, dtype=np.int16)
    for dy in range(3):
        for dx in range(3):
            r += ci * t[dy:dy+h, dx:dx+w]
            ci //= 2
    mp = key[r]
    if i == 1:
        print('Part 1:', np.sum(mp))

print('Part 2:', np.sum(mp))
