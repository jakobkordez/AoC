data = open('i04.txt').read().replace('\n', ' ').replace(':', ' ').split('  ')

req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

s1 = sum(set(f.split()[::2]).issuperset(req) for f in data)

print('Part 1:', s1)
