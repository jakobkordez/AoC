from aoc import *
from collections import defaultdict


class Node:
    def __init__(self):
        self.p: Node = None
        self.v = None
        self.vis = False
        self.c: list[Node] = []

    def getVal(self):
        if self.p is None:
            return 0
        if self.v is None:
            self.v = self.p.getVal() + 1
        return self.v

    def find(self, t: "Node"):
        if self.vis:
            return None
        self.vis = True
        if self is t:
            return -2
        for c in self.c:
            fv = c.find(t)
            if fv is not None:
                return fv + 1
        pv = self.p.find(t)
        if pv is not None:
            return pv + 1
        return None


data = read(6, ["\n", ")"])

dd = defaultdict(Node)

for a, b in data:
    dd[b].p = dd[a]
    dd[a].c.append(dd[b])

print("Part 1:", sum(v.getVal() for v in dd.values()))

print("Part 2:", dd["YOU"].find(dd["SAN"]))
