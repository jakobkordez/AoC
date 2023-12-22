from aoc import *
from collections import deque


class Block:
    leansOn: list["Block"]
    leanedOnBy: list["Block"]

    def __init__(self, pts: str):
        parsed = [map(int, xyz.split(",")) for xyz in pts.split("~")]
        (self.x1, self.y1, self.z1), (self.x2, self.y2, self.z2) = parsed
        self.leanedOnBy = []

    def overlaps(self, other: "Block"):
        x1 = max(self.x1, other.x1)
        x2 = min(self.x2, other.x2)
        if x1 > x2:
            return False
        y1 = max(self.y1, other.y1)
        y2 = min(self.y2, other.y2)
        return y1 <= y2


data: list[Block] = read(22, ["\n", Block])
data.sort(key=lambda x: x.z1)


stack: list[Block] = []

for block in data:
    leansOn: list[Block] = []
    maxZ = 0
    for other in stack:
        if other.z2 < maxZ:
            continue
        if not other.overlaps(block):
            continue
        if other.z2 > maxZ:
            leansOn = []
            maxZ = other.z2
        leansOn.append(other)
    for other in leansOn:
        other.leanedOnBy.append(block)
    block.leansOn = leansOn
    block.z2 += -block.z1 + maxZ + 1
    block.z1 = maxZ + 1
    stack.append(block)

p1 = 0
for block in stack:
    if all(len(other.leansOn) > 1 for other in block.leanedOnBy):
        p1 += 1
print("Part 1:", p1)

p2 = 0
for startingBrick in stack:
    q = deque(startingBrick.leanedOnBy)
    moved = set([startingBrick])
    while q:
        brick = q.popleft()
        if brick in moved:
            continue
        if all(b in moved for b in brick.leansOn):
            p2 += 1
            q.extend(brick.leanedOnBy)
            moved.add(brick)
print("Part 2:", p2)
