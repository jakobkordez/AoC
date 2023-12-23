from aoc import *

data = read(23, ["\n", list])

H, W = len(data), len(data[0])

data[0][1] = "#"
data[H - 1][W - 2] = "#"

dirs = {"v": (0, 1), "^": (0, -1), ">": (1, 0), "<": (-1, 0), "#": (0, 0)}


class Node:
    visited = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nbrs: list[tuple[int, "Node"]] = []

    def __repr__(self):
        return f"Node({self.x}, {self.y})"

    def dfs(self, end: "Node"):
        if self == end:
            return 2
        self.visited = True
        mx = -100000000
        for c, child in self.nbrs:
            if child.visited:
                continue
            mx = max(mx, child.dfs(end) + c)
        self.visited = False
        return mx


nodes: dict[tuple, Node] = dict()

start = nodes[(1, 1)] = Node(1, 1)
end = nodes[(W - 2, H - 2)] = Node(W - 2, H - 2)
for y in range(H - 1):
    for x in range(W):
        if data[y][x] == "#":
            continue
        c = sum(1 for dx, dy in FOUR_NEIGHBOURS if data[y + dy][x + dx] != "#")
        if c > 2:
            nodes[(x, y)] = Node(x, y)

p2 = []

for x, y in nodes:
    if nodes[(x, y)] == end:
        continue
    data[y][x] = "#"
    for dx, dy in FOUR_NEIGHBOURS:
        nx, ny = x + dx, y + dy
        if data[ny][nx] != "." and dirs[data[ny][nx]] != (dx, dy):
            continue
        c = 1
        while True:
            data[ny][nx] = "#"
            for dx, dy in FOUR_NEIGHBOURS:
                nnx, nny = nx + dx, ny + dy
                if data[nny][nnx] != "#":
                    nx, ny = nnx, nny
                    break
            c += 1
            if (nx, ny) in nodes:
                nodes[(x, y)].nbrs.append((c, nodes[(nx, ny)]))
                p2.append(((nx, ny), (x, y), c))
                break
    data[y][x] = "."

print("Part 1:", start.dfs(end))

for (x, y), (xx, yy), c in p2:
    nodes[(x, y)].nbrs.append((c, nodes[(xx, yy)]))

print("Part 2:", start.dfs(end))
