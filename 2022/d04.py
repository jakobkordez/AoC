from aoc import *

data = read('i04', ['\n', ',', '-'], int)

s1 = s2 = 0
for (l1, r1), (l2, r2) in data:
    ovl = min(r1, r2) - max(l1, l2)
    s1 += ovl == r1-l1 or ovl == r2-l2
    s2 += ovl >= 0

print('Part 1:', s1)
print('Part 2:', s2)
