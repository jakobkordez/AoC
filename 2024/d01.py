from aoc import *
from collections import Counter

data = read(1, ["\n", "   ", int])

cols = list(zip(*data))

print("Part 1:", sum(abs(b - a) for a, b in zip(*map(sorted, cols))))

c = Counter(cols[1])
print("Part 2:", sum(v * c[v] for v in cols[0]))
