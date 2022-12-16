from aoc import *
from random import randint, random, choice

data = read('i16', ['\n', ' '])

valves = [r[1] for r in data]
flows = [int(r[4][5:-1]) for r in data]
tunnels = [[valves.index(t.strip(',')) for t in r[9:]] for r in data]

memo = {}


def solve(currv, opened, time, mask):
    if time == 0:
        return 0
    key = (currv, time, mask, opened)

    if key not in memo:
        flow = flows[currv]
        mx = 0
        ii = 1 << currv
        if ii & opened == 0 and flow > 0:
            # Turn valve
            opened |= ii
            mx = solve(currv, opened, time - 1, mask) + flow * (time-1)
            opened ^= ii
        # Skip
        for nbr in tunnels[currv]:
            if (1 << nbr) & mask:
                mx = max(mx, solve(nbr, opened, time - 1, mask))
        memo[key] = mx

    return memo[key]


allm = (1 << len(valves)) - 1

start = valves.index('AA')

print('Part 1:', solve(start, 0, 30, allm))


def evalp2(mask):
    return solve(start, 0, 26, mask) + solve(start, 0, 26, allm ^ mask)


# Part 2 genetic algorithm
best = 0
pop_size = 100
cross = 0.2
mut = 0.2
pop = [randint(0, allm//2) for _ in range(pop_size)]
pop = [(evalp2(p), p) for p in pop]
pop.sort(reverse=True)
while True:
    next_pop = pop[:10]
    next_pop = []
    nrand = [randint(0, allm//2) for _ in range(10)]
    next_pop += [(evalp2(p), p) for p in nrand]
    for p in pop[:-20]:
        p = p[1]
        if random() < cross:
            p2 = choice(pop)[1]
            bi = randint(0, len(valves) - 1)
            mask = (1 << bi) - 1
            p = p & mask | p2 & (allm ^ mask)
        if random() < mut:
            p ^= 1 << randint(0, len(valves))
        next_pop.append((evalp2(p), p))
    pop = next_pop
    pop.sort(reverse=True)
    if pop[0][0] > best:
        best = pop[0][0]
        print(best)


# Part 2 naive (with memoization)
@functools.cache
def solve(currv, curre, opened, time):
    if time == 0:
        return 0

    flow = flows[currv]
    flowe = flows[curre]
    mx = 0
    ii = 1 << currv
    ie = 1 << curre
    if ii & opened == 0 and flow > 0:
        # Turn valve
        opened ^= ii
        if ie & opened == 0 and flowe > 0:
            # Elephant turn valve
            opened ^= ie
            mx = solve(currv, curre, opened, time - 1) + \
                (flow + flowe) * time
            opened ^= ie

        # Elephant skip
        for nbr in tunnels[curre]:
            mx = max(mx, solve(currv, nbr, opened,
                               time - 1) + flow * time)

        opened ^= ii

    if ie & opened == 0 and flowe > 0:
        # Only Elephant turn valve
        opened ^= ie
        for nbr in tunnels[currv]:
            mx = max(mx, solve(nbr, curre, opened,
                               time - 1) + flowe * time)
        opened ^= ie

    # Both Skip
    for nbr in tunnels[currv]:
        for nbre in tunnels[curre]:
            mx = max(mx, solve(nbr, nbre, opened, time - 1))
    return mx


print('Part 2:', solve(start, start, 0, 26))
