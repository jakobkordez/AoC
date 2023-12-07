from aoc import *
import re, string

data = read(1, ["\n"])

m = [" ", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", *string.digits]


def p1(x: str):
    x = list(map(int, re.findall(r"\d", x)))
    return x[0] * 10 + x[-1]


def p2(x: str):
    x = re.findall(f'(?=({"|".join(m)}))', x)
    x = list(map(lambda y: m.index(y) % 10, x))
    return x[0] * 10 + x[-1]


print("Part 1:", sum(map(p1, data)))
print("Part 2:", sum(map(p2, data)))
