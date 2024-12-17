from aoc import *
import re

(A, B, C), program = read(17, ["\n\n", re.compile("\d+"), int])


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


def go(val, i):
    if i < 0:
        return val
    mul = 8**i
    for k in range(8):
        t = val + mul * k
        res = solve(t)

        if res[i] != program[i]:
            continue

        res = go(t, i - 1)
        if res:
            return res


t = len(program) - 1
print("Part 2:", go(8**t, t))
