import re

with open('i17.txt') as file:
    x1, x2, y1, y2 = list(map(int, re.findall('-?\d+', file.read())))

sx = 1
while True:
    t = sx * (sx + 1) // 2
    if t >= x1 and t <= x2:
        break
    sx += 1


sy = -y1 - 1
print('Part 1:', sy * (sy + 1) // 2)

c = 0
for y in range(y1, -y1):
    for x in range(sx, x2 + 1):
        p = 0, 0
        d = y, x
        while p[0] >= y1 and p[1] <= x2:
            if p[0] >= y1 and p[0] <= y2 and p[1] >= x1 and p[1] <= x2:
                c += 1
                break
            p = p[0] + d[0], p[1] + d[1]
            d = d[0] - 1, max(0, d[1] - 1)

print('Part 2:', c)
