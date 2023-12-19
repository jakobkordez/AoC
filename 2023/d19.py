from aoc import *
import re
from math import prod

wfRaw, parts = read(19, ["\n\n", "\n"])

workflows = {}
for wf in wfRaw:
    name, insRaw, final = re.match(r"(\w+)\{((?:[\w<>]+:\w+,)*)(\w+)\}", wf).groups()
    instr = [ins.split(":") for ins in insRaw.split(",")[:-1]]
    workflows[name] = (instr, final)


def solve(wf, vars):
    if wf in "RA":
        return wf == "A"
    instr, final = workflows[wf]
    for test, target in instr:
        if eval(test, None, vars):
            return solve(target, vars)
    return solve(final, vars)


p1 = 0
for part in parts:
    part = re.sub(r"([xmas])=", r'"\1":', part)
    part: dict = eval(part)
    if solve("in", part):
        p1 += sum(part.values())

print("Part 1:", p1)


def solve2(wf, vars: dict[tuple]):
    if wf == "R":
        return 0
    if wf == "A":
        return prod(e - s + 1 for s, e in vars.values())

    instr, final = workflows[wf]
    sm = 0
    for test, target in instr:
        var, t, val = re.match(r"(\w+)([<>])(\d+)", test).groups()
        s, e = vars[var]
        ns, ne = s, e

        val = int(val)
        if t == "<" and e > val:
            ne = val - 1
            s = val
        elif t == ">" and s < val:
            ns = val + 1
            e = val

        if ns <= ne:
            nvars = vars.copy()
            nvars[var] = (ns, ne)
            sm += solve2(target, nvars)
        if s > e:
            break
        vars[var] = (s, e)
    else:
        sm += solve2(final, vars)
    return sm


vars = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
print("Part 2:", solve2("in", vars))
