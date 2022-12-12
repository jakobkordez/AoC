from aoc import *
from collections import deque

data = read('i12', ['\n', list])

h = len(data)
w = len(data[0])


def solve(q: deque):
    visited = {(x, y) for x, y, _ in q}

    while q:
        x, y, step = q.popleft()
        for dx, dy in FOUR_NEIGHBOURS:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if (nx, ny) in visited:
                continue
            if data[ny][nx] == 'E':
                if data[y][x] >= 'y':
                    return step + 1
            elif ord(data[ny][nx]) - ord(data[y][x]) <= 1:
                visited.add((nx, ny))
                q.append((nx, ny, step + 1))


p1 = deque()
p2 = deque()

for y in range(h):
    for x in range(w):
        if data[y][x] == 'S':
            p1.append((x, y, 0))
            data[y][x] = 'a'
        if data[y][x] == 'a':
            p2.append((x, y, 0))

print('Part 1:', solve(p1))
print('Part 2:', solve(p2))
