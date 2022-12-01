import numpy as np

with open('i03.txt') as file:
    data = np.array([list(a.strip()) for a in file.readlines()], dtype=np.int0)

bits = data.shape[1]                # Number of bits
bp = 2 ** np.arange(bits)[::-1]     # Helper array [.., 8, 4, 2, 1]

# Part 1
g = np.array([np.argmax(np.bincount(data[:, i])) for i in range(bits)])
print(sum(g * bp) * sum((1 - g) * bp))

# Part 2
ox = np.array(data)
for i in range(bits):
    bc = np.bincount(ox[:, i], minlength=2)
    ox = ox[np.where(ox[:, i] == (1 if bc[1] >= bc[0] else 0))]

coo = np.array(data)
for i in range(bits):
    bc = np.bincount(coo[:, i], minlength=2)
    coo = coo[np.where(coo[:, i] == (1 if bc[1] < bc[0] else 0))]
    if len(coo) == 1:
        break

print(sum(ox[0] * bp) * sum(coo[0] * bp))
