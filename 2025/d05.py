from aoc import *

fresh, ing = read(5, ["\n\n", "\n", "-", int])

print("Part 1:", sum(any(s <= x <= e for s, e in fresh) for (x,) in ing))


def combine(a1, a2, b1, b2):
    if b1 < a1:
        a1, a2, b1, b2 = b1, b2, a1, a2
    if a2 + 1 >= b1:
        return (a1, max(a2, b2))
    return None


combined = True
while combined:
    i = 0
    combined = False
    n = len(fresh)
    while i < n:
        j = i + 1
        while j < n:
            if cr := combine(*fresh[i], *fresh[j]):
                fresh[i] = cr
                fresh.pop(j)
                n -= 1
                combined = True
            else:
                j += 1
        i += 1
print("Part 2:", sum(e - s + 1 for s, e in fresh))
