from aoc import *
import re
import math
import multiprocessing as mp

# Bad solution, but it works
# Too slow and too much memory usage


def solve(blueprint, time):
    id, oreRore, clayRore, obsRore, obsRclay, geoRore, geoRobs = blueprint
    print('Blueprint', id)

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
    print('Done blueprint', id)
    memo.clear()
    return tmp


def solve1(b):
    return solve(b, 24) * b[0]


def solve2(b):
    return solve(b, 32)


if __name__ == '__main__':

    blueprints = read('i19', ['\n', re.compile(r'\d+')], int)

    with mp.Pool() as pool:
        print('Part 1:', sum(pool.map(solve1, blueprints)))

    with mp.Pool() as pool:
        print('Part 2:', math.prod(pool.map(solve2, blueprints[:3])))
