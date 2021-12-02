# Part 1

# First solution
c = 0
with open('i1.txt') as file:
    inp = list(map(int, file.readlines()))
for i in range(1, len(inp)):
    if inp[i] > inp[i-1]:
        c += 1
print(c)

# Two-liner
data = list(map(int, open('i1.txt').readlines()))
print([data[i-1] < data[i] for i in range(1, len(data))].count(True))


# Part 2

# First solution
c = 0
with open('i1.txt') as file:
    inp = list(map(int, file.readlines()))
for i in range(1, len(inp)-2):
    if sum(inp[i:i+3]) > sum(inp[i-1:i+2]):
        c += 1
print(c)

# Two-liner
data = list(map(int, open('i1.txt').readlines()))
print([data[i-3] < data[i] for i in range(3, len(data))].count(True))
