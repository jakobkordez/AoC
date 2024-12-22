from aoc import *
import numpy as np

data = [np.array(read(22, ["\n", int]), dtype=np.int64)]
for _ in range(2000):
    s = data[-1]
    s = ((s * 64) ^ s) % 16777216
    s = ((s // 32) ^ s) % 16777216
    s = ((s * 2048) ^ s) % 16777216
    data.append(s)
data = np.stack(data, 1)


print("Part 1:", sum(data[:, -1]))


data %= 10
diff = data[:, 1:] - data[:, :-1] + 10
key = diff[:, 3:] * 8000 + diff[:, 2:-1] * 400 + diff[:, 1:-2] * 20 + diff[:, :-3]

dd = np.zeros((160000), dtype=np.int16)
for j in range(len(data)):
    s = np.zeros((160000), dtype=np.int16)
    s[key[j, ::-1]] = data[j, :3:-1]
    dd += s

print("Part 2:", max(dd))
