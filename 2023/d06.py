from aoc import *
import re
from math import prod, floor, sqrt


# O(t) brute force
def solveBF(t, p):
    return sum(i * (t - i) > p for i in range(1, t))


# O(t) faster brute force
def solveBF2(t, p):
    return t - 2 * next(i for i in range(1, t) if i * (t - i) > p) + 1


# O(log(t)) binary search
def solveBS(t, p):
    return t - 2 * binarySearch(1, t // 2, lambda m: m * (t - m) > p) + 1


# O(log(t)) because of sqrt
def solveMath(t, p):
    return t - 2 * floor((t - sqrt(t * t - 4 * p)) / 2) - 1


data = read(6, ["\n", re.compile(r"\d+"), int])
print("Part 1:", prod(solveBS(*x) for x in zip(*data)))

data = read(6, ["\n", re.compile(r"\d")])
print("Part 2:", solveBS(*map(int, map("".join, data))))
