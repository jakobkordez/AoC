from aoc import *
from heapq import heappop, heappush

data = read(9, [list, int])

free = []
full = []


def rangeSum(a, b):
    return (b * (b - 1)) // 2 - (a * (a - 1)) // 2


pos = 0
for i, d in enumerate(data):
    pr = (pos, pos + d)
    pos += d
    if i & 1:
        free.append(pr)
    else:
        full.append(pr)

free_copy = list(free)
full_copy = list(full)

free_i = 0
full_i = len(full) - 1

p1 = 0
while free[free_i][0] < full[full_i][1]:
    freeL, freeR = free[free_i]
    fullL, fullR = full[full_i]
    maxMove = min(freeR - freeL, fullR - fullL)
    p1 += full_i * rangeSum(freeL, freeL + maxMove)
    freeL += maxMove
    fullR -= maxMove
    if freeL == freeR:
        free_i += 1
    else:
        free[free_i] = (freeL, freeR)
    if fullL == fullR:
        full_i -= 1
    else:
        full[full_i] = (fullL, fullR)

while full_i >= 0:
    fullL, fullR = full[full_i]
    p1 += full_i * rangeSum(fullL, fullR)
    full_i -= 1

print("Part 1:", p1)


full = list(full_copy)
free = [[] for _ in range(10)]
for l, r in free_copy:
    heappush(free[r - l], l)

p2 = 0
for full_i in range(len(full) - 1, 0, -1):
    fullL, fullR = full[full_i]
    fullLen = fullR - fullL

    min_i = 0
    min_v = fullL
    for i in range(fullLen, 10):
        if free[i][0] < min_v:
            min_i = i
            min_v = free[i][0]

    if min_i != 0:
        heappop(free[min_i])
        if min_i > fullLen:
            heappush(free[min_i - fullLen], min_v + fullLen)
        full[full_i] = (min_v, min_v + fullLen)

    p2 += full_i * rangeSum(*full[full_i])

print("Part 2:", p2)
