with open('d1.txt') as f:
    file = f.read().strip()

elves = [sum(map(int, elf.split())) for elf in file.split('\n\n')]

print('Part 1:', max(elves))
print('Part 2:', sum(sorted(elves)[-3:]))
