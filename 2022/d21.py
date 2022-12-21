from aoc import *
from functools import cache

monkeys = {}
for n, op in read('i21', ['\n', ': ']):
    if '0' <= op[0] <= '9':
        monkeys[n] = int(op)
    else:
        monkeys[n] = op.split()


def solve(name):
    op = monkeys[name]
    if type(op) == int:
        return op
    v1, v2 = solve(op[0]), solve(op[2])
    match op[1]:
        case '+': return v1 + v2
        case '-': return v1 - v2
        case '*': return v1 * v2
        case '/': return v1 // v2
        case '=': return v1 == v2


print('Part 1:', solve('root'))


def solve2(name, prev=None):
    op = monkeys[name]
    p = [n for n, v in monkeys.items() if type(v) is not int and name in v]
    if p == []:
        return solve(op[2] if op[0] == prev else op[0])
    target = solve2(p[0], name)
    if prev is None:
        return target
    othr = solve(op[0] if op[0] != prev else op[2])
    match op[1]:
        case '+': return target - othr
        case '-': return (target + othr) if op[0] == prev else (othr - target)
        case '*': return target // othr
        case '/': return (target * othr) if op[0] == prev else (othr // target)


print('Part 2:', solve2('humn'))
