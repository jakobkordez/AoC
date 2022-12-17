from aoc import *

data = read('i16', ['\n', ' '])

valves = [r[1] for r in data]
flows = [int(r[4][5:-1]) for r in data]
tunnels = [[valves.index(t.strip(',')) for t in r[9:]] for r in data]

memo = {}
solutions = {}


def solve(currv, opened, time, score):
    if time < 1:
        solutions[opened] = max(solutions.get(opened, 0), score)
        return 0, opened
    key = (currv, time, opened)

    if key not in memo:
        flow = flows[currv]
        ii = 1 << currv
        mx = 0
        bestopen = opened
        if ii & opened == 0 and flow > 0:
            # Turn valve
            tmx, topen = solve(currv, opened | ii, time -
                               1, score + flow * (time-1))
            # tmx += flow * (time-1)
            if tmx > mx:
                mx, bestopen = tmx, topen
        # Skip
        for nbr in tunnels[currv]:
            tmx, topen = solve(nbr, opened, time - 1, score)
            if tmx > mx:
                mx, bestopen = tmx, topen
        memo[key] = mx, bestopen

    mx, bestopen = memo[key]
    solutions[bestopen] = max(solutions.get(bestopen, 0), mx + score)

    return memo[key]


start = valves.index('AA')

solve(start, 0, 30, 0)
print('Part 1:', max(solutions.values()))

memo.clear()
solutions.clear()

solve(start, 0, 26, 0)
p2 = 0
for mask1, v1 in solutions.items():
    for mask2, v2 in solutions.items():
        if mask1 & mask2 == 0:
            p2 = max(p2, v1 + v2)

print('Part 2:', p2)
