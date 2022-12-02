from aoc import *


def scmap(a):
    return ord(a) - 64


s1 = s2 = 0

beats = {
    'B': 'A',
    'C': 'B',
    'A': 'C'
}

for p, m in read('i02', ['\n', ' ']):
    t = chr(ord(m) - 23)
    s1 += scmap(t)
    if p == t:
        s1 += 3
    elif beats[t] == p:
        s1 += 6

    match m:
        case 'X': s2 += scmap(beats[p])
        case 'Y': s2 += scmap(p) + 3
        case 'Z': s2 += scmap({y: x for x, y in beats.items()}[p]) + 6

print('Part 1:', s1)
print('Part 2:', s2)
