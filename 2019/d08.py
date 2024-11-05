from aoc import *

data = read(8)

min0 = 25 * 6 + 1
res = None
for layer in splitByCount(data, 25 * 6):
    zeros = layer.count("0")
    if zeros < min0:
        min0 = zeros
        res = layer.count("1") * layer.count("2")
print("Part 1:", res)

p = [[False] * 25 for _ in range(6)]
for layer in splitByCount(data, 25 * 6)[::-1]:
    for y in range(6):
        for x in range(25):
            if layer[y * 25 + x] == "1":
                p[y][x] = True
            elif layer[y * 25 + x] == "0":
                p[y][x] = False

print("Part 2:")
for y in range(6):
    for x in range(25):
        print("#" if p[y][x] else " ", end=" ")
    print()
