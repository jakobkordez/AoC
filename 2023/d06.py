from aoc import *
import re
from math import prod, ceil, sqrt


# O(t) brute force
def solveBF(t, p):
    c = 0
    for i in range(1, t):
        if i * (t - i) >= p:
            c += 1
    return c


# O(log(t)) binary search
def solveBS(t, p):
    a = 1
    b = t // 2
    while a < b:
        m = (a + b) // 2
        if m * (t - m) < p:
            a = m + 1
        else:
            b = m
    return t - 2 * a + 1


# O(log(t)) because of sqrt
def solveMath(t, p):
    return t - 2 * ceil((t - sqrt(t**2 - 4 * p)) / 2) + 1


data = zip(*read("i06", ["\n", re.compile(r"\d+")], int))
print("Part 1:", prod(map(lambda x: solveBS(*x), data)))

data = read("i06", ["\n", re.compile(r"\d")])
t, p = map(lambda x: int("".join(x)), data)

print("Part 2:", solveBS(t, p))
