from aoc import *
from itertools import combinations, count
from functools import cache
from collections import defaultdict
import numpy as np
import re

data = read(10, ["\n", " "])


def splitNum(s):
    return split(s, [re.compile("\d+"), int])


def solveRow(ind, bts, jolt):
    ind = sum(2**i for i, e in enumerate(ind[1:]) if e == "#")
    jolt = splitNum(jolt)

    def prepareBtn(btn):
        p = np.zeros(len(jolt), dtype=np.int_)
        p[btn] = 1
        return p

    bts = list(map(prepareBtn, map(splitNum, bts)))

    combs = [(prepareBtn([]), 0)]
    for r in range(1, len(bts) + 1):
        for b_comb in combinations(bts, r):
            combs.append((np.sum(b_comb, axis=0), r))

    dd = defaultdict(lambda: [])
    for c, r in combs:
        dd[sum((c % 2) * 2 ** np.arange(len(c)))].append((c, r))

    @cache
    def solve(jolt):
        if all(e == 0 for e in jolt):
            return 0
        if any(e < 0 for e in jolt):
            return 999999
        p2 = 999999
        tmp = sum(2**i for i, e in enumerate(jolt) if e % 2 == 1)
        for b_comb, r in dd[tmp]:
            joltNew = (np.array(jolt) - b_comb) // 2
            p2 = min(p2, r + 2 * solve(tuple(joltNew)))
        return p2

    return min(r for _, r in dd[ind]), solve(tuple(jolt))


solved = list(map(sum, zip(*[solveRow(ind, bts, jolt) for ind, *bts, jolt in data])))
print("Part 1:", solved[0])
print("Part 2:", solved[1])
