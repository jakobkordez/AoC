from aoc import *
import re
from math import prod, ceil
import multiprocessing as mp
import argparse

# Bad solution, but it works
# Too slow and too much memory usage


def solve(blueprint, time):
    _, oreRore, clayRore, obsRore, obsRclay, geoRore, geoRobs = blueprint

    memo = {}

    def f(time, ore=0, clay=0, obs=0, oreR=1, clayR=0, obsR=0):
        if time <= 1:
            return 0
        key = (time, ore, clay, obs, oreR, clayR, obsR)
        if key in memo:
            return memo[key]

        best = 0
        # Buy geode robot if possible
        if obsR > 0:
            treq = max(ceil(max(0, geoRore - ore) / oreR),
                       ceil(max(0, geoRobs - obs) / obsR)) + 1
            best = f(time - treq,
                     ore + oreR * treq - geoRore,
                     clay + clayR * treq,
                     obs + obsR * treq - geoRobs,
                     oreR, clayR, obsR) + (time - treq)
        # Buy ore robot
        treq = ceil(max(0, oreRore - ore) / oreR) + 1
        temp = f(time - treq,
                 ore + oreR * treq - oreRore,
                 clay + clayR * treq,
                 obs + obsR * treq,
                 oreR + 1, clayR, obsR)
        best = max(best, temp)
        # Buy clay robot
        treq = ceil(max(0, clayRore - ore) / oreR) + 1
        temp = f(time - treq,
                 ore + oreR * treq - clayRore,
                 clay + clayR * treq,
                 obs + obsR * treq,
                 oreR, clayR + 1, obsR)
        best = max(best, temp)
        # Buy obsidian robot if possible
        if clayR > 0:
            treq = max(ceil(max(0, obsRore - ore) / oreR),
                       ceil(max(0, obsRclay - clay) / clayR)) + 1
            temp = f(time - treq,
                     ore + oreR * treq - obsRore,
                     clay + clayR * treq - obsRclay,
                     obs + obsR * treq,
                     oreR, clayR, obsR + 1)
            best = max(best, temp)

        memo[key] = best
        return best

    tmp = f(time)
    memo.clear()
    return tmp


def solvee(p):
    b, time = p
    print('Solving blueprint', b[0], 'with time', time, '...')
    tmp = solve(b, time)
    print('Done blueprint', b[0], 'with time', time)
    return tmp


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store_true')
    args = parser.parse_args()

    blueprints = read('i19', ['\n', re.compile(r'\d+')], int)

    if args.p:
        with mp.Pool() as pool:
            bparams = blueprints[:3] + blueprints
            tparams = [32] * 3 + [24] * len(blueprints)
            r = pool.map(solvee, zip(bparams, tparams))

        print('Part 1:', sum(s * b[0] for s, b in zip(r[3:], blueprints)))
        print('Part 2:', prod(r[:3]))
    else:
        print('Part 1:', sum(solvee((b, 24)) * b[0] for b in blueprints))
        print('Part 2:', prod(solvee((b, 32)) for b in blueprints[:3]))
