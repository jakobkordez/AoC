from aoc import *
from collections import deque

drop = read('i18', ['\n', ','], int)

field = [[[1] * 30 for _ in range(30)] for _ in range(30)]
for x, y, z in drop:
    field[z + 1][y + 1][x + 1] = 0


q = deque([(0, 0, 0)])
while q:
    x, y, z = q.popleft()
    if field[z][y][x] != 1:
        continue
    field[z][y][x] = 2
    for dx, dy, dz in SIX_NEIGHBOURS:
        nx, ny, nz = x + dx, y + dy, z + dz
        if nx < 0 or ny < 0 or nz < 0 or nx >= 30 or ny >= 30 or nz >= 30:
            continue
        q.append((nx, ny, nz))


p1 = p2 = 0
for x, y, z in drop:
    for dx, dy, dz in SIX_NEIGHBOURS:
        nbr = field[z + dz + 1][y + dy + 1][x + dx + 1]
        p1 += nbr > 0
        p2 += nbr > 1

print('Part 1:', p1)
print('Part 2:', p2)
