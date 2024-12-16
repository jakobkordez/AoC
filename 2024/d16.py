from aoc import *
from heapq import *

data = read(16, ["\n", list])
H, W = len(data), len(data[0])

FY, FX = 1, W - 2
SY, SX = H - 2, 1

heap = []
visited = dict()


def pushMaybe(score, x, y, dx, dy):
    k = (x, y, dx, dy)
    if k not in visited:
        visited[k] = score
        heappush(heap, (score, x, y, dx, dy))


pushMaybe(0, SX, SY, 1, 0)

while heap[0][1] != FX or heap[0][2] != FY:
    score, x, y, dx, dy = heappop(heap)
    if data[y + dy][x + dx] != "#":
        pushMaybe(score + 1, x + dx, y + dy, dx, dy)
    pushMaybe(score + 1000, x, y, -dy, dx)
    pushMaybe(score + 1000, x, y, dy, -dx)

print("Part 1:", heap[0][0])


heap = [heap[0]]
spotCount = set()
while heap:
    score, x, y, dx, dy = heap.pop()
    if visited.get((x, y, dx, dy)) != score:
        continue
    spotCount.add((x, y))
    visited[(x, y, dx, dy)] = 0
    if data[y - dy][x - dx] != "#":
        heap.append((score - 1, x - dx, y - dy, dx, dy))
    heap.append((score - 1000, x, y, -dy, dx))
    heap.append((score - 1000, x, y, dy, -dx))


print("Part 2:", len(spotCount))
