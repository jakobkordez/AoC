from aoc import *
import re
from collections import deque, defaultdict
from math import prod, lcm

data = read(20, ["\n", " -> "])

flipMemo = defaultdict(lambda: False)
conjMemo = defaultdict(lambda: {})

tiles = {}
for head, ch in data:
    typ, name = re.match(r"([%&]?)(\w+)", head).groups()
    ch = ch.split(", ")
    tiles[name] = (typ, ch)
    for c in ch:
        conjMemo[c][name] = False


# Graphviz code
# tiles["rx"] = ("", "")
# typMap = {"%": "F_", "&": "N_", "": ""}
# for name, (typ, ch) in tiles.items():
#     for c in ch:
#         print(f"{typMap[typ]}{name} -> {typMap[tiles[c][0]]}{c};")


pulseCounter = [0, 0]
counter = 0
countDict = {}


def press():
    global counter, pulseCounter
    counter += 1

    q = deque([("button", "broadcaster", False)])
    while q:
        source, name, pulse = q.popleft()
        pulseCounter[pulse] += 1
        if name not in tiles:
            continue
        typ, ch = tiles[name]
        if typ == "":
            q.extend((name, c, pulse) for c in ch)
        elif typ == "%" and not pulse:
            outPulse = not flipMemo[name]
            flipMemo[name] = outPulse
            q.extend((name, c, outPulse) for c in ch)
        elif typ == "&":
            conjMemo[name][source] = pulse
            outPulse = not all(conjMemo[name].values())
            if outPulse:
                countDict.setdefault(name, counter)
            q.extend((name, c, outPulse) for c in ch)


for _ in range(1000):
    press()
print("Part 1:", prod(pulseCounter))


for _ in range(4000):
    press()
print("Part 2:", lcm(*countDict.values()))
