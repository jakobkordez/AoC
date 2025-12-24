from aoc import *
from itertools import combinations, count
from functools import cache
import numpy as np
import re

data = read(10, ["\n", " "])


def splitNum(s):
    return split(s, [re.compile("\d+"), int])


def solveRow(ind, bts, jolt):
    ind = sum(2**i for i, e in enumerate(ind[1:]) if e == "#")
    bts = [sum(2**n for n in btn) for btn in map(splitNum, bts)]
    jolt = splitNum(jolt)

    def allCombinations(p, check):
        for r in range(len(p) + 1):
            for b_comb in combinations(p, r):
                res = 0
                for btn in b_comb:
                    res ^= btn
                if res == check:
                    yield b_comb

    for b_comb in allCombinations(bts, ind):
        p1 = len(b_comb)
        break

    @cache
    def solve(jolt):
        if all(e == 0 for e in jolt):
            return 0
        if any(e < 0 for e in jolt):
            return 999999
        p2 = 999999
        tmp = sum(2**i for i, e in enumerate(jolt) if e % 2 == 1)
        for b_comb in allCombinations(bts, tmp):
            joltNew = list(jolt)
            for btn in b_comb:
                i = 0
                while btn > 0:
                    joltNew[i] -= btn % 2
                    btn //= 2
                    i += 1
            for i in range(len(joltNew)):
                joltNew[i] //= 2
            p2 = min(p2, len(b_comb) + 2 * solve(tuple(joltNew)))
        return p2

    return p1, solve(tuple(jolt))


solved = list(map(sum, zip(*[solveRow(ind, bts, jolt) for ind, *bts, jolt in data])))
print("Part 1:", solved[0])
print("Part 2:", solved[1])
