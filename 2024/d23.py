from aoc import *
from collections import defaultdict

data = read(23, ["\n", "-"])

nodes = defaultdict(lambda: set())

for a, b in data:
    nodes[a].add(b)
    nodes[b].add(a)


p1 = 0
for a, b in data:
    overlap = nodes[a] & nodes[b]
    if not overlap:
        continue
    if a[0] == "t" or b[0] == "t":
        p1 += len(overlap)
    else:
        p1 += sum(e[0] == "t" for e in overlap)
print("Part 1:", p1 // 3)


nItems = list(nodes.items())
cache = {}


def go(party: set, i=0):
    key = ",".join(sorted(party))
    if key in cache:
        return cache[key]
    m = party
    for j, (n, nSet) in enumerate(nItems[i:]):
        if n in m or not party.issubset(nSet):
            continue
        r = go({*party, n}, i + j + 1)
        if len(r) > len(m):
            m = r
    cache[key] = m
    return m


print("Part 2:", ",".join(sorted(go(set()))))
