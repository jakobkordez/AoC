from aoc import *

sack = read('i03', ['\n'])


def pr(x):
    return -38 % ord(*x) % 58


s1 = 0
for s in sack:
    n = len(s)//2
    s1 += pr({*s[:n]} & {*s[n:]})

s2 = 0
for s in range(0, len(sack), 3):
    a, b, c = map(set, sack[s:s+3])
    s2 += pr(a & b & c)

print('Part 1:', s1)
print('Part 2:', s2)
