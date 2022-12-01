import numpy as np

with open('i07.txt') as file:
    d = np.array(file.read().split(','), dtype=np.int32)

p1 = p2 = np.inf
for i in range(min(d), max(d) + 1):
    n = np.abs(d - i)
    p1 = min(p1, np.sum(n))
    p2 = min(p2, np.sum(n*(n+1)//2))

print('Part 1:', p1)
print('Part 2:', p2)

n = np.array([abs(d-i) for i in range(max(d)+1)])
print('Part 1:', min(np.sum(n, axis=1).T))
print('Part 2:', min(np.sum(n * (n+1) // 2, axis=1).T))

# O(n*lb(n))
print('Part 1:', np.sum(abs(d - np.median(d)), dtype=np.int32))
n = abs(np.ceil(d - np.average(d)))
print('Part 2:', np.sum(n*(n+1)//2, dtype=np.int32))
