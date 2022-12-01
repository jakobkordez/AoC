from math import prod

with open('i16.txt') as file:
    data = file.read()
    d = bin(int(data, 16))[2:].zfill(len(data) * 4)

verSum = 0
i = 0


def decode():
    global i, verSum
    ver = int(d[i: i+3], 2)
    id = int(d[i+3: i+6], 2)
    i += 6
    verSum += ver
    if id == 4:
        lit = 0
        while d[i] == '1':
            lit = (lit << 4) + int(d[i+1: i+5], 2)
            i += 5
        lit = (lit << 4) + int(d[i+1: i+5], 2)
        i += 5
        return lit
    else:
        lenTypeID = d[i] == '1'
        i += 1
        lits = []
        if not lenTypeID:
            totalLen = int(d[i:i+15], 2) + i + 15
            i += 15
            while i < totalLen:
                lits.append(decode())
        else:
            subPack = int(d[i: i+11], 2)
            i += 11
            while subPack > 0:
                lits.append(decode())
                subPack -= 1
        if id == 0:
            return sum(lits)
        if id == 1:
            return prod(lits)
        if id == 2:
            return min(lits)
        if id == 3:
            return max(lits)
        a, b = lits
        if id == 5:
            return 1 if a > b else 0
        if id == 6:
            return 1 if a < b else 0
        if id == 7:
            return 1 if a == b else 0


r = decode()
print('Part 1:', verSum)
print('Part 2:', r)
