import numpy as np

with open('i06.txt') as file:
    data = np.array(file.read().strip().split(','), dtype=np.int64)

# Smart
sma = list(np.bincount(data, minlength=9))

for i in range(256):
    sma[7] += sma[0]
    sma = sma[1:] + [sma[0]]
    if i + 1 == 80:
        print('Part 1:', sum(sma))

print('Part 2:', sum(sma))

# Initial
cc = np.ones_like(data, dtype=np.int64)

for i in range(256):
    res = data == 0
    data = np.append(np.where(res, 6, data - 1), [8])
    cc = np.append(cc, [sum(np.where(res, cc, 0))])
    if i + 1 == 80:
        print('Part 1:', np.sum(cc))

print('Part 2:', np.sum(cc))
