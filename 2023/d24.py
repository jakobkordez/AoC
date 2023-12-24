from aoc import *
import z3

data = read(24, ["\n", " @ ", ", ", int])

MIN = 200000000000000
MAX = 400000000000000


def isOn(px, py, x, y, dx, dy):
    dx = clamp(-1, dx, 1)
    dy = clamp(-1, dy, 1)
    dxx = clamp(-1, px - x, 1)
    dyy = clamp(-1, py - y, 1)
    return dx == dxx and dy == dyy


p1 = 0
for i, ((x1, y1, z1), (dx1, dy1, dz1)) in enumerate(data):
    k1 = dy1 / dx1
    n1 = y1 - k1 * x1
    for (x2, y2, z2), (dx2, dy2, dz2) in data[i + 1 :]:
        k2 = dy2 / dx2
        n2 = y2 - k2 * x2
        if k1 == k2:
            continue
        x = (n2 - n1) / (k1 - k2)
        y = k1 * x + n1
        if x < MIN or x > MAX or y < MIN or y > MAX:
            continue
        if isOn(x, y, x1, y1, dx1, dy1) and isOn(x, y, x2, y2, dx2, dy2):
            p1 += 1

print("Part 1:", p1)

s = z3.Solver()

x = z3.Real("x")
y = z3.Real("y")
z = z3.Real("z")
dx = z3.Real("dx")
dy = z3.Real("dy")
dz = z3.Real("dz")

for i, ((xi, yi, zi), (dxi, dyi, dzi)) in enumerate(data):
    t = z3.Real(f"t_{i}")
    s.add(x + dx * t == xi + dxi * t)
    s.add(y + dy * t == yi + dyi * t)
    s.add(z + dz * t == zi + dzi * t)

s.check()
m = s.model()
print("Part 2:", sum(int(str(m[r])) for r in [x, y, z]))
