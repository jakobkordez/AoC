from aoc import *

data = read(3, ["\n", ",", lambda x: (x[0], int(x[1:]))])

w1 = [(0, 0)]
for d, l in data[0]:
    x, y = w1[-1]
    if d == "U":
        y += l
    elif d == "D":
        y -= l
    elif d == "L":
        x -= l
    elif d == "R":
        x += l
    w1.append((x, y))

w2 = [(0, 0)]
for d, l in data[1]:
    x, y = w2[-1]
    if d == "U":
        y += l
    elif d == "D":
        y -= l
    elif d == "L":
        x -= l
    elif d == "R":
        x += l
    w2.append((x, y))


def overlap(a1, a2, b1, b2):
    if a1 > a2:
        a1, a2 = a2, a1
    if b1 > b2:
        b1, b2 = b2, b1
    if a1 <= b2 and b1 <= a2:
        return max(a1, b1), min(a2, b2)


overlaps = []
p1 = 0
for i in range(len(w1) - 1):
    (x1, y1), (x2, y2) = w1[i : i + 2]
    p2 = 0
    for j in range(len(w2) - 1):
        (x3, y3), (x4, y4) = w2[j : j + 2]
        ox = overlap(x1, x2, x3, x4)
        oy = overlap(y1, y2, y3, y4)
        if ox and oy and ox[0] != 0 and oy[0] != 0:
            ox, oy = ox[0], oy[0]
            pp1 = p1 + abs(x1 - ox) + abs(y1 - oy)
            pp2 = p2 + abs(x3 - ox) + abs(y3 - oy)
            overlaps.append((ox, oy, pp1, pp2))
        p2 += abs(x3 - x4) + abs(y3 - y4)
    p1 += abs(x2 - x1) + abs(y2 - y1)

print("Part 1:", min(abs(x) + abs(y) for x, y, *_ in overlaps))
print("Part 2:", min(pp1 + pp2 for _, _, pp1, pp2 in overlaps))
