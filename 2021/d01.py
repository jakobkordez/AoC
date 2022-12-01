with open('i01.txt') as file:
    data = list(map(int, file.readlines()))

print('Part 1:', [data[i-1] < data[i]
      for i in range(1, len(data))].count(True))
print('Part 2:', [data[i-3] < data[i]
      for i in range(3, len(data))].count(True))
