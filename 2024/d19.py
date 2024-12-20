from aoc import *
import re
from functools import cache

towels, patterns = read(19, ["\n\n", re.compile("[a-z]+")])


class Trie:
    def __init__(self):
        self.c: dict[str, Trie] = dict()
        self.e = False

    def add(self, s: str):
        if s == "":
            self.e = True
        else:
            self.c.setdefault(s[0], Trie())
            self.c[s[0]].add(s[1:])

    def get(self, s: str, d=0):
        ret = []
        if s != "" and s[0] in self.c:
            ret.extend(self.c[s[0]].get(s[1:], d + 1))
        if self.e:
            ret.append(d)
        return ret


root = Trie()
for t in towels:
    root.add(t)


@cache
def solve(pattern: str):
    if pattern == "":
        return 1
    return sum(solve(pattern[t:]) for t in root.get(pattern))


r = list(map(solve, patterns))
print("Part 1:", sum(map(bool, r)))
print("Part 2:", sum(r))
