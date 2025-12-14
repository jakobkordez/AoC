from aoc import *
import re

*shapes, regions = read(12, ["\n\n", "\n", re.compile("\d+"), int])


print("Part 1:", sum((h // 3) * (w // 3) >= sum(p) for h, w, *p in regions))
