from aoc import *
from collections import Counter

start, end = read(4, ["-", int])


def test(x):
    x = str(x)
    double = False
    for i in range(len(x) - 1):
        if x[i] == x[i + 1]:
            double = True
        if x[i] > x[i + 1]:
            return False
    return double


print("Part 1:", sum(map(test, range(start, end + 1))))


def test2(x):
    x = str(x)
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            return False
    return 2 in Counter(x).values()


print("Part 2:", sum(map(test2, range(start, end + 1))))
