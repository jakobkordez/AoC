from aoc import *


def split(s: str):
    return (-1 if "L" in s else 1) * int(s[1:])


data = read(1, ["\n", split])

p1 = p2 = 0
c = 50

for n in data:
    if n < 0 and c == 0:
        p2 -= 1
    c += n
    if c <= 0:
        p2 -= (c - 1) // 100
    else:
        p2 += c // 100
    c %= 100
    if c == 0:
        p1 += 1

print("Part 1:", p1)
print("Part 2:", p2)
