from aoc import *
from collections import Counter

data = read(1, [str.split, int])

print("Part 1:", sum(abs(b - a) for a, b in zip(sorted(data[::2]), sorted(data[1::2]))))

c = Counter(data[1::2])
print("Part 2:", sum(v * c[v] for v in data[::2]))
