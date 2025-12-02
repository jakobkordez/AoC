from aoc import *

data = read(2, [",", "-", int])


def solve(m):
    for s, e in data:
        i = 1
        while (n := int(str(i) * m)) < e:
            if n >= s:
                yield n
            i += 1


def solvePart(n):
    return sum({r for e in range(2, n + 1) for r in solve(e)})


print("Part 1:", solvePart(2))
print("Part 2:", solvePart(max(len(str(e)) for _, e in data)))
