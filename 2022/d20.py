from aoc import *

origCoords = read('i20', ['\n'], int)
N = len(origCoords)


def solve(part2):
    decrKey = 811589153 if part2 else 1
    coords = [[x*decrKey, None, None] for x in origCoords]
    zeroi = coords.index([0, None, None])
    for i in range(N):
        coords[i][1] = coords[(i - 1) % N]
        coords[i][2] = coords[(i + 1) % N]

    rounds = 10 if part2 else 1
    for _ in range(rounds):
        for i in range(N):
            curr = coords[i]
            pr = curr[1]
            nx = curr[2]
            pr[2] = nx
            nx[1] = pr
            for _ in range(abs(curr[0]) % (N - 1)):
                if curr[0] > 0:
                    nx = nx[2]
                else:
                    nx = nx[1]
            pr = nx[1]
            nx[1] = curr
            curr[2] = nx
            curr[1] = pr
            pr[2] = curr

    sol = 0
    curr = coords[zeroi]
    for i in range(3):
        for _ in range(1000 % N):
            curr = curr[2]
        sol += curr[0]
    return sol


print('Part 1:', solve(False))
print('Part 2:', solve(True))
