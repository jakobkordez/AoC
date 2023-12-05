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
                overlapStart = max(rStart, sStart)
                overlapEnd = min(rEnd, sStart + dsLen)
                if overlapStart >= overlapEnd:
                    continue
                overlapLen = overlapEnd - overlapStart
                overlapOffset = overlapStart - sStart

                newRanges.append([dStart + overlapOffset, overlapLen])
                if overlapStart != rStart:
                    ranges.append([rStart, overlapStart - rStart])
                if overlapEnd != rEnd:
                    ranges.append([overlapEnd, rEnd - overlapEnd])

                break
            else:
                newRanges.append([rStart, rLen])

        ranges = deque(newRanges)

    return min(ranges)[0]


print("Part 1:", solve(map(lambda x: [x, 1], seeds)))
print("Part 2:", solve(splitByCount(seeds, 2)))
