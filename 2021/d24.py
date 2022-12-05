with open('i24.txt') as f:
    prog = [*map(str.split, f.read().strip().split('\n'))]

pp = [[int(prog[18*i+j][2]) for j in [4, 5, 15]] for i in range(14)]

mm = [1]
for i in range(13, 0, -1):
    mm.insert(0, pp[i][0] * mm[0])


def _go(i, z, w, rng):
    p = pp[i]
    x = z % 26 + p[1] != w
    z //= p[0]
    z *= 25 * x + 1
    z += (w + p[2]) * x
    if z >= mm[i]:
        return None
    if i == 13:
        return f'{w}'
    for nw in rng:
        r = _go(i+1, z, nw, rng)
        if r != None:
            return f'{w}{r}'


def go(rng):
    for w in rng:
        r = _go(0, 0, w, rng)
        if r != None:
            return r


print('This might take a minute...')
print('Part 1:', go(range(9, 0, -1)))
print('Part 2:', go(range(1, 10)))
