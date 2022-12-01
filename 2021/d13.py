with open('i13.txt') as file:
    a, b = file.read().strip().split('\n\n')

t = dict()
for aa in a.split('\n'):
    x, y = list(map(int, aa.split(',')))
    t[y, x] = True

p1 = False
for bb in b.split('\n'):
    ax, p = bb.split()[-1].split('=')
    p = int(p)
    for (y, x), v in list(t.items()):
        if not v:
            continue
        if ax == 'x':
            if x <= p:
                continue
            t[y, x] = False
            t[y, 2*p - x] = True
            rig = p
        elif ax == 'y':
            if y <= p:
                continue
            t[y, x] = False
            t[2*p - y, x] = True
            bot = p
    if not p1:
        p1 = True
        print('Part 1:', sum(t.values()))

print('Part 2:')
for y in range(bot):
    for x in range(rig):
        print('#' if t.get((y, x), False) else ' ', end=' ')
    print()
