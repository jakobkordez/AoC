from itertools import cycle

inp = [e-1 for e in [10, 7]]

p = [*inp]
dr = 0
s = [0, 0]
for r in cycle(range(1, 101)):
    pi = dr//3 % 2
    p[pi] += r
    if dr % 3 == 2:
        p[pi] %= 10
        s[pi] += p[pi] + 1
        if s[pi] >= 1000:
            break
    dr += 1

print('Part 1:', min(s) * (dr + 1))


memo = {}


def go(p1, p2, s1, s2):
    mem_key = (p1, p2, s1, s2)

    if s2 >= 21:
        return 0, 1

    if mem_key not in memo:
        p1ss = p2ss = 0
        for x in range(1, 4):
            for y in range(1, 4):
                for z in range(1, 4):
                    np1 = (p1 + x + y + z) % 10
                    t2, t1 = go(p2, np1, s2, s1 + np1 + 1)
                    p1ss += t1
                    p2ss += t2
        memo[mem_key] = p1ss, p2ss

    return memo[mem_key]


print('Part 2:', max(go(*inp, 0, 0)))
