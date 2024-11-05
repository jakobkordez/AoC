from aoc import *
from copy import copy

originalData = read(2, [",", int])


def run(noun: int, verb: int) -> int:
    data = copy(originalData)

    data[1] = noun
    data[2] = verb

    i = 0
    while True:
        if data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
            i += 4
        elif data[i] == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
            i += 4
        elif data[i] == 99:
            return data[0]
        else:
            raise Exception("Invalid instruction")


print("Part 1:", run(12, 2))

for noun in range(100):
    for verb in range(100):
        if run(noun, verb) == 19690720:
            print("Part 2:", noun * 100 + verb)
            break
    else:
        continue
    break
