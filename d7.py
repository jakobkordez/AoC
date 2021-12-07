import numpy as np

with open('i7.txt') as file:
    data = np.array(file.read().split(','), dtype=np.int32)

p1 = p2 = np.inf
for i in range(min(data), max(data) + 1):
    n = np.abs(data - i)
    p1 = min(p1, np.sum(n))
    p2 = min(p2, np.sum(n*(n+1)//2))

print('Part 1:', p1)
print('Part 2:', p2)
