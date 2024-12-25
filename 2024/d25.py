from aoc import *
import numpy as np

data = read(25, ["\n\n", "\n", list])

data = np.array(data) == "#"

keys = np.sum(data[np.where(data[:, 0, 0])], 1)
locks = np.sum(data[np.where(data[:, 0, 0] == False)], 1)

res = 0
for i in range(len(locks)):
    res += np.count_nonzero(np.all(keys + np.roll(locks, i, 0) <= 7, 1))
print("Part 1:", res)
