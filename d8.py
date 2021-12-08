from itertools import groupby

with open('i8.txt') as file:
    d = [[a.split() for a in l.split(' | ')] for l in file.readlines()]

dd = [0] * 8
for i, o in d:
    for oo in o:
        dd[len(oo)] += 1

print('Part 1:', dd[2] + dd[3] + dd[4] + dd[7])


def group(i, key):
    return {k: list(v) for k, v in groupby(sorted(i, key=key), key=key)}


sm = 0
for i, o in d:
    i = [set(a) for a in i]
    nb = [None] * 10
    nb[8] = next(filter(lambda x: len(x) == 7, i))
    nb[1] = next(filter(lambda x: len(x) == 2, i))
    nb[4] = next(filter(lambda x: len(x) == 4, i))
    nb[7] = next(filter(lambda x: len(x) == 3, i))

    s = group(filter(lambda x: x not in nb, i), lambda x: nb[1].issubset(x))
    # 2 5 6
    s0 = group(s[False], len)
    nb[6] = s0[6][0]
    nb[5] = next(filter(lambda x: x.issubset(nb[6]), s0[5]))
    nb[2] = next(filter(lambda x: x not in nb, s0[5]))
    # 0 3 9
    s1 = group(s[True], len)
    nb[3] = s1[5][0]
    nb[9] = next(filter(lambda x: nb[4].issubset(x), s1[6]))
    nb[0] = next(filter(lambda x: x not in nb, s1[6]))

    sm += int(''.join([str(nb.index(set(a))) for a in o]))

print('Part 2:', sm)
