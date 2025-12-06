from aoc import *
from math import prod

data = [(list(map(int, n)), op) for *n, op in zip(*read(6, ["\n", str.split]))]

print("Part 1:", sum(sum(n) if op == "+" else prod(n) for n, op in data))


data = [
    (int("".join(n)), op)
    for *n, op in zip(*read(6, ["\n", list], rstrip="\n"))
    if any(e != " " for e in n)
][::-1]


sm = 0
tsm = []
for d, op in data:
    tsm.append(d)
    if op == "+":
        sm += sum(tsm)
        tsm = []
    elif op == "*":
        sm += prod(tsm)
        tsm = []
print("Part 2:", sm)
