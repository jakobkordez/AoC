from aoc import *
import numpy as np

data = read(25, ["\n\n", "\n", list])

data = np.array(data) == "#"
N = len(data)

res = N * (N + 1) // 2
for i in range(N):
    res -= sum(np.any(data[i:] & data[: N - i], (1, 2)))
print("Part 1:", res)
