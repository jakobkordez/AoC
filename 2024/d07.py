from aoc import *
import re
import numpy as np

data = read(7, ["\n", re.compile(r"\d+"), int])


p = [10] * 10 + [100] * 90 + [1000] * 900

p1 = p2 = 0
for res, *vals in data:
    arr = np.array([vals[0]], dtype=np.int64)
    for n in vals[1:]:
        arr = np.concatenate([arr + n, arr * n])
    if res in arr:
        p1 += res
        continue

    arr = np.array([vals[0]], dtype=np.int64)
    for n in vals[1:]:
        arr = np.concatenate([arr + n, arr * n, arr * p[n] + n])
    if res in arr:
        p2 += res

print("Part 1:", p1)
print("Part 2:", p1 + p2)
