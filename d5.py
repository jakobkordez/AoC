import re
import numpy as np

with open('i5.txt') as file:
    data = [list(map(int, re.split(r'\D+', l.strip())))
            for l in file.readlines()]

s = np.zeros((1000, 1000), dtype=np.int32)
d = np.zeros((1000, 1000), dtype=np.int32)
for x1, y1, x2, y2 in data:
    xs, xl = sorted([x1, x2])
    ys, yl = sorted([y1, y2])
    if y1 == y2:
        s[y1, xs:xl + 1] += 1
    elif x1 == x2:
        s[ys:yl + 1, x1] += 1
    else:
        d[ys:yl + 1, xs:xl + 1] += np.rot90(np.identity(
            xl - xs + 1, dtype=np.int32), 1 if (x1 > x2) != (y1 > y2) else 0)

print('Part 1:', np.sum(s > 1))
print('Part 2:', np.sum(s + d > 1))
