from aoc import *

msg = read('i06')


def findUnique(x):
    for i in range(len(msg)):
        if len({*msg[i:i+x]}) == x:
            return i + x


print('Part 1:', findUnique(4))
print('Part 2:', findUnique(14))
