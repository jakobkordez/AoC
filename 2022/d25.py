from aoc import *


def from_snafu(snafu):
    m = 1
    ret = 0
    for e in snafu[::-1]:
        match e:
            case '-': e = -1
            case '=': e = -2
            case _: e = int(e)
        ret += e * m
        m *= 5
    return ret


def to_snafu(n):
    ret = ''
    while n:
        d = n % 5
        if d == 4:
            n += 1
        elif d == 3:
            n += 3
        ret += '=-012'[(d+2) % 5]
        n //= 5
    return ret[::-1]


values = read('i25', ['\n'], from_snafu)

print('Part 1:', to_snafu(sum(values)))
