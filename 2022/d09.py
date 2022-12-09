from aoc import *

moves = read('i09', ['\n', ' '])


def solve(length):
    chain = [(0, 0) for _ in range(length)]
    sol = set()

    for d, c in moves:
        for _ in range(int(c)):
            hx, hy = chain[0]
            match d:
                case 'U': hy += 1
                case 'D': hy -= 1
                case 'L': hx -= 1
                case 'R': hx += 1
            chain[0] = (hx, hy)

            for i in range(1, length):
                hx, hy = chain[i-1]
                tx, ty = chain[i]
                if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                    tx += clamp(-1, hx - tx, 1)
                    ty += clamp(-1, hy - ty, 1)
                chain[i] = (tx, ty)

            sol.add(chain[-1])

    return len(sol)


print('Part 1:', solve(2))
print('Part 2:', solve(10))
