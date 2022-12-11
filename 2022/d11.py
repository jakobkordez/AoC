from aoc import *
from math import prod

data = read('i11', ['\n\n', '\n'])

starting = [[*map(int, m[1][18:].split(', '))] for m in data]

monkeys = []
for m in data:
    oper = m[2][19:]
    test = int(m[3][21:])
    deci = [int(l.split()[-1]) for l in m[4:]]
    monkeys += [[oper, test, deci]]


def solve(rounds, evals):
    obs = [0] * len(monkeys)
    holding = [[*m] for m in starting]

    for _ in range(rounds):
        for i, (_, test, deci) in enumerate(monkeys):
            obs[i] += len(holding[i])
            for val in map(evals[i], holding[i]):
                holding[deci[val % test > 0]] += [val]
            holding[i] = []

    return prod(sorted(obs)[-2:])


evals = [eval(f'lambda old: ({m[0]}) // 3') for m in monkeys]
print('Part 1:', solve(20, evals))

mod = prod(m[1] for m in monkeys)
evals = [eval(f'lambda old: ({m[0]}) % {mod}') for m in monkeys]
print('Part 2:', solve(10000, evals))
