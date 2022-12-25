from aoc import *


def from_snafu(s):
    return sum(('=-012'.find(e) - 2) * 5**i for i, e in enumerate(s[::-1]))


def to_snafu(n):
    ret = ''
    while n:
        d = n % 5
        ret += '012=-'[d]
        n = n//5 + (d > 2)
    return ret[::-1]


values = read('i25', ['\n'], from_snafu)

print('Part 1:', to_snafu(sum(values)))
