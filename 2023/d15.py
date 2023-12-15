from aoc import *
import re

data = read(15, [","])


def hash(r):
    h = 0
    for c in r:
        h = (h + ord(c)) * 17
    return h % 256


print("Part 1:", sum(map(hash, data)))

parser = re.compile(r"([a-z]+)([\-=])(\d?)")
boxes = [dict() for _ in range(256)]

for r in data:
    lb, op, f = parser.match(r).groups()
    if op == "=":
        boxes[hash(lb)][lb] = f
    else:
        boxes[hash(lb)].pop(lb, None)

p2 = 0
for bi, box in enumerate(boxes):
    for fi, f in enumerate(box.values()):
        p2 += (bi + 1) * (fi + 1) * int(f)

print("Part 2:", p2)
