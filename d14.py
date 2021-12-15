import numpy as np

with open('i14.txt') as file:
    t, insr = file.read().strip().split('\n\n')

ins = dict()
for a in insr.split('\n'):
    a, b = a.split(' -> ')
    c, d = list(a)
    ins[ord(c), ord(d)] = ord(b)


d = [ord(c) for c in t]
for _ in range(10):
    td = [d[0]]
    for i in range(1, len(d)):
        td += [ins[d[i-1], d[i]], d[i]]
    d = td

d = np.array(d)
_, c = np.unique(d, return_counts=True)

print('Part 1:', max(c) - min(c))


cache = dict()


def rec(a, b, i):
    if i == 0:
        return {b: 1}
    if cache.get((a, b, i), None) != None:
        return cache[a, b, i]
    tmp = ins[a, b]
    f = dict(rec(a, tmp, i-1))
    s = rec(tmp, b, i-1)
    for sk, sv in s.items():
        f[sk] = f.get(sk, 0) + sv
    cache[a, b, i] = f
    return f


r = dict()
d = [ord(c) for c in t]
for i in range(1, len(d)):
    for k, v in rec(d[i-1], d[i], 40).items():
        r[k] = r.get(k, 0) + v

print('Part 2:', max(r.values()) - min(r.values()))
