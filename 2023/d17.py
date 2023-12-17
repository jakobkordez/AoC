from aoc import *
import heapq

data = read(17, ["\n", list, int])

H, W = len(data), len(data[0])


def solve(max_s, min_s: int = 0, data=data, H=H, W=W):
    seen = set()
    q = [(0, 1, 0, 1, 1), (0, 0, 1, 2, 1)]
    heapq.heapify(q)
    while q:
        d, x, y, dr, t = heapq.heappop(q)
        if x < 0 or x >= W or y < 0 or y >= H:
            continue
        if (x, y, dr, t) in seen:
            continue
        seen.add((x, y, dr, t))
        d += data[y][x]
        if x == W - 1 and y == H - 1 and t >= min_s:
            return d
        if t < max_s:
            dx, dy = FOUR_NEIGHBOURS[dr]
            heapq.heappush(q, (d, x + dx, y + dy, dr, t + 1))
        if t >= min_s:
            lft = (dr - 1) % 4
            dx, dy = FOUR_NEIGHBOURS[lft]
            heapq.heappush(q, (d, x + dx, y + dy, lft, 1))
            rgt = (dr + 1) % 4
            dx, dy = FOUR_NEIGHBOURS[rgt]
            heapq.heappush(q, (d, x + dx, y + dy, rgt, 1))


print("Part 1:", solve(3))
print("Part 2:", solve(10, 4))
