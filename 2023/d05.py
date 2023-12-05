from aoc import *
from collections import deque

seeds, *stepsRaw = read("i05", ["\n\n"])

seeds = list(map(int, seeds.split(": ")[1].split()))

steps = []
for step in stepsRaw:
    rgs = step.split("\n")[1:]
    steps.append([*map(lambda x: list(map(int, x.split())), rgs)])


def solve(seedR):
    ranges = deque(seedR)

    for step in steps:
        newRanges = []
        while ranges:
            rStart, rLen = ranges.pop()
            rEnd = rStart + rLen

            for dStart, sStart, dsLen in step:
                oStart = max(rStart, sStart)
                oEnd = min(rEnd, sStart + dsLen)
                if oStart >= oEnd:
                    continue

                newRanges.append([dStart + oStart - sStart, oEnd - oStart])
                if oStart != rStart:
                    ranges.append([rStart, oStart - rStart])
                if oEnd != rEnd:
                    ranges.append([oEnd, rEnd - oEnd])

                break
            else:
                newRanges.append([rStart, rLen])

        ranges = deque(newRanges)

    return min(ranges)[0]


print("Part 1:", solve(map(lambda x: [x, 1], seeds)))
print("Part 2:", solve(splitByCount(seeds, 2)))
