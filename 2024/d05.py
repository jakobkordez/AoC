from aoc import *
import re
from collections import defaultdict

rules, updates = read(5, ["\n\n", "\n", re.compile(r"\d+"), int])

rd = defaultdict(lambda: set())
for a, b in rules:
    rd[a].add(b)


def valid(pages: list[int]):
    s = set()
    for p in pages:
        if len(s & rd[p]) > 0:
            return False
        s.add(p)
    return True


print("Part 1:", sum(u[len(u) // 2] for u in updates if valid(u)))


def fixedMiddle(pages: list[int]):
    retry = True
    while retry:
        retry = False
        s = dict()
        for i, p in enumerate(pages):
            frst = i
            for rde in rd[p]:
                if rde in s:
                    frst = min(frst, s[rde])
            if frst != i:
                pages[i], pages[frst] = pages[frst], pages[i]
                retry = True
            s.setdefault(p, i)
    return pages[len(pages) // 2]


print("Part 2:", sum(fixedMiddle(u) for u in updates if not valid(u)))
