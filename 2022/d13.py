from aoc import *

data = read('i13', ['\n\n', '\n'], eval)


def compare(a, b) -> int:
    if type(a) is int and type(b) is int:
        return a - b
    if type(a) is int:
        a = [a]
    elif type(b) is int:
        b = [b]
    for i in range(min(len(a), len(b))):
        cmp = compare(a[i], b[i])
        if cmp != 0:
            return cmp
    return len(a) - len(b)


s1 = sum(i+1 for i, pair in enumerate(data) if compare(*pair) < 0)
print('Part 1:', s1)

p = qsorted(sum(data, [0, 2, 6]), compare)
print('Part 2:', p.index(2) * p.index(6))
