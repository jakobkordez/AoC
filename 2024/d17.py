from aoc import *
import re
from functools import cache

(A, B, C), program = read(17, ["\n\n", re.compile("\d+"), int])


@cache
def solve(a, b=B, c=C):
    def combo(op):
        match op:
            case 0 | 1 | 2 | 3:
                return op
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c
            case 7:
                return None

    stk = []
    ip = 0
    while ip < len(program):
        match program[ip]:
            case 0:
                a //= 2 ** combo(program[ip + 1])
                ip += 2
            case 1:
                b ^= program[ip + 1]
                ip += 2
            case 2:
                b = combo(program[ip + 1]) & 0b111
                ip += 2
            case 3:
                if a != 0:
                    ip = program[ip + 1]
                else:
                    ip += 2
            case 4:
                b ^= c
                ip += 2
            case 5:
                stk.append(combo(program[ip + 1]) & 0b111)
                ip += 2
            case 6:
                b = a // 2 ** combo(program[ip + 1])
                ip += 2
            case 7:
                c = a // 2 ** combo(program[ip + 1])
                ip += 2
    return stk


print("Part 1:", ",".join(map(str, solve(A))))


def go(bot, top, i):
    if i < 0:
        return bot
    for m in range(bot, top, 8 ** max(0, i - 1)):
        res = solve(m)
        if res[i:] != program[i:]:
            continue

        a = bot
        b = m
        while a + 1 < b:
            m = (a + b) // 2
            res = solve(m)
            if res[i:] != program[i:]:
                a = m
            else:
                b = m
        bot = b

        a = bot
        b = top
        while a + 1 < b:
            m = (a + b) // 2
            res = solve(m)
            if res[i:] != program[i:]:
                b = m
            else:
                a = m
        top = b

        res = go(bot, top, i - 1)
        if res:
            return res


bot = 0o1
while len(solve(bot)) != len(program):
    bot *= 8

print("Part 2:", go(bot, bot * 8, len(program) - 1))
