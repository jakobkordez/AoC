from aoc import *
from functools import cache

data = read(11, [" ", int])


@cache
def blink(d, count=25):
    if count == 0:
        return 1
    if d == 0:
        return blink(1, count - 1)
    s = str(d)
    ls = len(s)
    if ls % 2 == 0:
        ls //= 2
        return blink(int(s[:ls]), count - 1) + blink(int(s[ls:]), count - 1)
    return blink(d * 2024, count - 1)


print("Part 1:", sum(blink(d) for d in data))
print("Part 2:", sum(blink(d, 75) for d in data))
