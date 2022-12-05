from aoc import *

stacks, rules = read('i05', ['\n\n', '\n'])

p1 = [[] for _ in range(9)]
for line in stacks[-2::-1]:
    for i, e in enumerate(line[1::4]):
        if e != ' ':
            p1[i] += [e]

p2 = [[*stk] for stk in p1]


for line in rules:
    a, b, c = map(int, line.split()[1::2])
    fr1, fr2 = p1[b-1], p2[b-1]
    to1, to2 = p1[c-1], p2[c-1]
    to1.extend(fr1[:-a-1:-1])
    del fr1[-a:]
    to2.extend(fr2[-a:])
    del fr2[-a:]


print('Part 1:', ''.join(e[-1] for e in p1))
print('Part 2:', ''.join(e[-1] for e in p2))
