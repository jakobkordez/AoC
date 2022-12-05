with open('i25.txt') as f:
    p = [[*l] for l in f.read().split()]

h, w = len(p), len(p[0])

anyMoved = True
i = 0
ch = '>v'
while True:
    if i % 2 == 0:
        if not anyMoved:
            break
        anyMoved = False

    dx, dy = (1, 0) if i % 2 == 0 else (0, 1)

    op = p
    p = [[*l] for l in p]
    for y in range(h):
        for x in range(w):
            if op[y][x] == ch[i % 2] and op[(y+dy) % h][(x+dx) % w] == '.':
                p[(y+dy) % h][(x+dx) % w] = ch[i % 2]
                p[y][x] = '.'
                anyMoved = True
    i += 1

# *map(print, map(''.join, p)),

print('Part 1:', i // 2)
