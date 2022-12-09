data = open('i03.txt').readlines()

s1 = sum(p[(i*3) % 31] == '#' for i, p in enumerate(data))

print('Part 1:', s1)

s2 = s1

for dx, dy in [(1, 1), (5, 1), (7, 1), (1, 2)]:
    s2 *= sum(p[(i*dx) % 31] == '#' for i, p in enumerate(data[::dy]))

print('Part 2:', s2)
