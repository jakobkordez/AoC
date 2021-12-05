import re
import numpy as np

with open('i5.txt') as file:
    data = [list(map(int, re.split(r'\D+', l.strip())))
            for l in file.readlines()]

s = np.zeros((1000, 1000), dtype=np.int32)
d = np.zeros((1000, 1000), dtype=np.int32)
for x1, y1, x2, y2 in data:
    for i in range(max(abs(y2 - y1) + 1, abs(x2 - x1) + 1)):
        if y1 == y2:
            s[y1][min(x1, x2) + i] += 1
        elif x1 == x2:
            s[min(y1, y2) + i][x1] += 1
        else:
            d[y1 + (i if y1 < y2 else -i)][x1 + (i if x1 < x2 else -i)] += 1

print('Part 1:', np.sum(s > 1))
print('Part 2:', np.sum(s + d > 1))
