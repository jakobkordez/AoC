from aoc import *
import re
from math import prod
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

        # If possible buy geode robot
        if ore >= geoRore and obs >= geoRobs:
            best = f(time - 1, ore + oreR - geoRore, clay + clayR,
                     obs + obsR - geoRobs, oreR, clayR, obsR) + (time - 1)
        else:
            # Buy nothing
            best = f(time - 1,
                     ore + oreR, clay + clayR, obs + obsR,
                     oreR, clayR, obsR)
            # Buy ore robot
            if ore >= oreRore:
                temp = f(time - 1,
                         ore + oreR - oreRore, clay + clayR, obs + obsR,
                         oreR + 1, clayR, obsR)
                best = max(best, temp)
            # Buy clay robot
            if ore >= clayRore:
                temp = f(time - 1,
                         ore + oreR - clayRore, clay + clayR, obs + obsR,
                         oreR, clayR + 1, obsR)
                best = max(best, temp)
            # Buy obsidian robot
            if ore >= obsRore and clay >= obsRclay:
                temp = f(time - 1,
                         ore + oreR - obsRore, clay + clayR - obsRclay, obs + obsR,
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
