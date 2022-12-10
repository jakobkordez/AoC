from aoc import *

instr = read('i10', ['\n', ' '])

reg = 1
cy = 1

s1 = 0
s2 = ''


def ex(arg=None):
    global reg, cy, s1, s2
    s2 += '# ' if reg-1 <= (cy - 1) % 40 <= reg+1 else '  '
    if arg:
        reg += int(arg)
    cy += 1
    if cy % 40 == 20:
        s1 += cy * reg


for cmd, *arg in instr:
    ex()
    if cmd == 'addx':
        ex(*arg)


print('Part 1:', s1)
print('Part 2:', *splitByCount(s2, 80), sep='\n')
