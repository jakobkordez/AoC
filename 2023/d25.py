from aoc import *
from random import choice
from math import prod, ceil
from copy import deepcopy

data = read(25, ["\n", ": ", " "])

edges = list()

for (r,), cc in data:
    for c in cc:
        edges.append([r, c])


# Karger's algorithm
# Randomly pick an edge and merge the two vertices
def Karger(edges: list[list[str]], t: int, d: dict[str, int]):
    edges = deepcopy(edges)
    d = dict(d)
    V = len(d)

    while V > t:
        r, c = choice(edges)
        d[r] += d[c]
        del d[c]
        V -= 1
        for e in edges:
            if e[0] == c:
                e[0] = r
            if e[1] == c:
                e[1] = r
        edges = [e for e in edges if e[0] != e[1]]

    return edges, d


def fastMinCut(edges: list[list[str]], d: dict[str, int]):
    V = len(d)
    if V <= 6:
        return Karger(edges, 2, d)
    t = ceil(1 + V / 2)
    e1, d1 = fastMinCut(*Karger(edges, t, d))
    if len(e1) == 3:
        return e1, d1
    return fastMinCut(*Karger(edges, t, d))


d = dict()
for r, c in edges:
    d[r] = d[c] = 1

while True:
    n, p = fastMinCut(edges, d)
    if len(n) == 3:
        print("Part 1:", prod(p.values()))
        break
