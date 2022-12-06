from collections import deque

with open('i19.txt') as f:
    scn = [[(*map(int, line.split(',')),) for line in sc.split()[4:]]
           for sc in f.read().strip().split('\n\n')]

N = len(scn)
MIN_OVERLAP = 12


def rot90z(coords):
    return [(-y, x, z) for x, y, z in coords]


def rot90x(coords):
    return [(x, -z, y) for x, y, z in coords]


def rot90y(coords):
    return [(z, y, -x) for x, y, z in coords]


def getAllOrient(coords):
    for _ in range(4):
        for _ in range(4):
            yield coords
            coords = rot90z(coords)
        coords = rot90x(coords)
    coords = rot90y(coords)
    for _ in range(4):
        yield coords
        coords = rot90z(coords)
    coords = rot90y(rot90y(coords))
    for _ in range(4):
        yield coords
        coords = rot90z(coords)


def mapToPairs(coords):
    for x1, y1, z1 in coords:
        for x2, y2, z2 in coords:
            if x1 == x2 and y1 == y2 and z1 == z2:
                continue
            yield x2-x1, y2-y1, z2-z1


def mapDelta(arr, dx, dy, dz):
    return [(x+dx, y+dy, z+dz) for x, y, z in arr]


def findMapedDeltas(a, b, ovl=None):
    if ovl is None:
        ovl = MIN_OVERLAP
    for ax, ay, az in a:
        for bx, by, bz in b:
            maped = mapDelta(b, ax-bx, ay-by, az-bz)
            if overlap(a, maped) >= ovl:
                return maped, ax-bx, ay-by, az-bz


def overlap(a, b):
    a = {*a}
    c = 0
    for e in b:
        if e in a:
            a.remove(e)
            c += 1
    return c


scnOr = [list(getAllOrient(sc)) for sc in scn]

scwor = [[list(mapToPairs(o)) for o in s] for s in scnOr]

prs = []
for i in range(N):
    print('Precheck:', i, '/', N, end='\r')
    for j in range(i + 1, N):
        for bo in scwor[j]:
            if overlap(scwor[i][0], bo) >= MIN_OVERLAP * (MIN_OVERLAP - 1):
                prs += [(i, j)]
                break
print(end='Precheck: Done     \r')

curr = {*scn[0]}
q = deque(x[1] for x in prs if x[0] == 0)
done = set([0]+[*q])
scnpos = [(0, 0, 0)]

while q:
    print('Done:', len(done)-len(q), '/', N, end='      \r')
    i = q.popleft()
    for o in getAllOrient(scn[i]):
        r = findMapedDeltas(curr, o)
        if r:
            maped, *dp = r
            curr.update(maped)
            scnpos += [dp]
            for a, b in prs:
                if b == i:
                    a, b = b, a
                if a == i and b not in done:
                    q.append(b)
                    done.add(b)
            break

print('Part 1:', len(curr), '   ')

mx = 0
for x1, y1, z1 in scnpos:
    for x2, y2, z2 in scnpos:
        mx = max(mx, abs(x1-x2)+abs(y1-y2)+abs(z1-z2))

print('Part 2:', mx)
