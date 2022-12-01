from aoc import *

elves = [*map(sum, read('i01', ['\n\n', '\n'], int))]

print('Part 1:', max(elves))
print('Part 2:', sum(sorted(elves)[-3:]))
