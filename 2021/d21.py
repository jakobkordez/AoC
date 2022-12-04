from itertools import cycle

p = [9, 6]

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
