with open('i02.txt') as file:
    data = file.readlines()

# Part 1
p, d = 0, 0
for c in data:
    a, b = c.strip().split()
    if a == 'forward':
        p += int(b)
    elif a == 'down':
        d += int(b)
    elif a == 'up':
        d -= int(b)
        if d < 0:
            d = 0
print('Part 1:', d * p)

# Part 2
p, d, a = 0, 0, 0
for c in data:
    c, x = c.strip().split()
    if c == 'forward':
        p += int(x)
        d += a * int(x)
    elif c == 'down':
        a += int(x)
    elif c == 'up':
        a -= int(x)
print('Part 2:', d * p)
