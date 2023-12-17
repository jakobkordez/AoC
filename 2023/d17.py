from aoc import *
import heapq

data = read(17, ["\n", list, int])

H, W = len(data), len(data[0])


def solve(max_s, min_s: int = 0, data=data, H=H, W=W):
    seen = set()
    q = [(0, 1, 0, 1), (0, 0, 1, 2)]
    heapq.heapify(q)
    while q:
        d, x, y, dr = heapq.heappop(q)
        if x < 0 or x >= W or y < 0 or y >= H:
            continue
        if dr == -1:
            return d
        if (x, y, dr) in seen:
            continue
        seen.add((x, y, dr))
        dx, dy = FOUR_NEIGHBOURS[dr]
        for dist in range(1, max_s + 1):
            if x < 0 or x >= W or y < 0 or y >= H:
                break
            d += data[y][x]
            if dist >= min_s:
                if x == W - 1 and y == H - 1:
                    heapq.heappush(q, (d, x, y, -1))
                    break
                lft = (dr - 1) % 4
                fx, fy = FOUR_NEIGHBOURS[lft]
                heapq.heappush(q, (d, x + fx, y + fy, lft))
                rgt = (dr + 1) % 4
                fx, fy = FOUR_NEIGHBOURS[rgt]
                heapq.heappush(q, (d, x + fx, y + fy, rgt))
            x += dx
            y += dy


print("Part 1:", solve(3))
print("Part 2:", solve(10, 4))
