from aoc import *
from copy import copy
from itertools import permutations

originalData = read(7, [",", int])


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


class Amp:
    def __init__(self, data: list[int], inputs: list[int]):
        self.data = data
        self.i = 0
        self.inputs = inputs
        self.output = []

    def run(self) -> bool:
        while True:
            opcode = self.data[self.i] % 100
            if opcode == 1:
                a, b, c = parseParams(self.data, self.i, 3)
                self.data[c] = self.data[a] + self.data[b]
                self.i += 4
            elif opcode == 2:
                a, b, c = parseParams(self.data, self.i, 3)
                self.data[c] = self.data[a] * self.data[b]
                self.i += 4
            elif opcode == 3:
                if len(self.inputs) == 0:
                    return False
                (a,) = parseParams(self.data, self.i, 1)
                self.data[a] = self.inputs.pop(0)
                self.i += 2
            elif opcode == 4:
                (a,) = parseParams(self.data, self.i, 1)
                self.output.append(self.data[a])
                self.i += 2
            elif opcode == 5:
                a, b = parseParams(self.data, self.i, 2)
                if self.data[a] != 0:
                    self.i = self.data[b]
                else:
                    self.i += 3
            elif opcode == 6:
                a, b = parseParams(self.data, self.i, 2)
                if self.data[a] == 0:
                    self.i = self.data[b]
                else:
                    self.i += 3
            elif opcode == 7:
                a, b, c = parseParams(self.data, self.i, 3)
                self.data[c] = 1 if self.data[a] < self.data[b] else 0
                self.i += 4
            elif opcode == 8:
                a, b, c = parseParams(self.data, self.i, 3)
                self.data[c] = 1 if self.data[a] == self.data[b] else 0
                self.i += 4
            elif opcode == 99:
                return True
            else:
                raise Exception("Invalid instruction", self.data[self.i])


best = 0
for phase in permutations(range(5)):
    val = 0
    phase = list(phase)
    for _ in range(5):
        amp = Amp(copy(originalData), [phase.pop(), val])
        amp.run()
        val = amp.output[0]
    if val > best:
        best = val
print("Part 1:", best)


best = 0
for phases in permutations(range(5, 10)):
    amps = [Amp(copy(originalData), [phase]) for phase in phases]
    amps[-1].output.append(0)
    while True:
        for i, amp in enumerate(amps):
            amp.inputs.append(amps[i - 1].output[-1])
            done = amp.run()
        if done:
            break
    val = amps[-1].output[-1]
    if val > best:
        best = val
print("Part 2:", best)
