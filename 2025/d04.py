from aoc import *
import numpy as np

data = (np.array(read(4, ["\n", list])) == "@") * 1
h, w = data.shape


def rm():
    global data
    adj = np.zeros_like(data)
    for dx, dy in EIGHT_NEIGHBOURS:
        adj += np.pad(data, 1)[dy + 1 : h + dy + 1, dx + 1 : w + dx + 1]
    rm = adj < 4 * data
    tot = np.sum(rm)
    data -= rm
    return tot


c = rm()
print("Part 1:", c)
while t := rm():
    c += t
print("Part 2:", c)
