from aoc import *
from copy import copy

originalData = read(5, [",", int])


def parseParams(data: list[int], i: int, n: int) -> list[int]:
    params = []
    t = data[i] // 100
    for x in range(n):
        a = i + x + 1
        if t & 1 == 0:
            a = data[a]
        params.append(a)
        t //= 10
    return params


def run(inputVal: int) -> list[int]:
    data = copy(originalData)

    output = []

    i = 0
    while True:
        opcode = data[i] % 100
        if opcode == 1:
            a, b, c = parseParams(data, i, 3)
            data[c] = data[a] + data[b]
            i += 4
        elif opcode == 2:
            a, b, c = parseParams(data, i, 3)
            data[c] = data[a] * data[b]
            i += 4
        elif opcode == 3:
            (a,) = parseParams(data, i, 1)
            data[a] = inputVal
            i += 2
        elif opcode == 4:
            (a,) = parseParams(data, i, 1)
            output.append(data[a])
            i += 2
        elif opcode == 5:
            a, b = parseParams(data, i, 2)
            if data[a] != 0:
                i = data[b]
            else:
                i += 3
        elif opcode == 6:
            a, b = parseParams(data, i, 2)
            if data[a] == 0:
                i = data[b]
            else:
                i += 3
        elif opcode == 7:
            a, b, c = parseParams(data, i, 3)
            data[c] = 1 if data[a] < data[b] else 0
            i += 4
        elif opcode == 8:
            a, b, c = parseParams(data, i, 3)
            data[c] = 1 if data[a] == data[b] else 0
            i += 4
        elif opcode == 99:
            return output
        else:
            raise Exception("Invalid instruction", data[i])


print("Part 1:", run(1))
print("Part 2:", run(5))