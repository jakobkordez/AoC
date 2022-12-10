import re
from aoc import *

instr = re.sub(r'[a-z]+', '0', read('i10')).split()

reg = 1
cy = 1

s1 = 0
s2 = ''

for e in instr:
    s2 += '# ' if reg-1 <= (cy - 1) % 40 <= reg+1 else '  '
    reg += int(e)
    cy += 1
    if cy % 40 == 20:
        s1 += cy * reg


print('Part 1:', s1)
print('Part 2:', *splitByCount(s2, 80), sep='\n')
