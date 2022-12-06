with open('i23.txt') as f:
    lines = [line[3:10:2] for line in f.read().strip().split('\n')[2:-1]]
    lines = [[ord(c)-65 for c in line] for line in lines[::-1]]
    s = [*map(list, zip(*lines))]
    temp = [-1] * 11


def play(state: list[list[int]], temp: list[int]) -> int:
    state = [[*e] for e in state]
    temp = [*temp]
    cost = 0
    # Check any determenistic moves
    check = True
    while check:
        check = False
        for i in range(4):
            if not all(e == i for e in state[i]):
                continue
            c = l = r = 2*i + 2
            while l > 0 and temp[l] == -1:
                l -= 1
            while r < 10 and temp[r] == -1:
                r += 1
            if temp[l] == i:
                cost += 10**i * (ROWS - len(state[i]) + c - l)
                state[i].append(i)
                temp[l] = -1
                check = True
            if temp[r] == i:
                cost += 10**i * (ROWS - len(state[i]) + r - c)
                state[i].append(i)
                temp[r] = -1
                check = True
            for j in range(4):
                if i == j:
                    continue
                a, b = sorted([2*i+2, 2*j+2])
                if state[j] and state[j][-1] == i and all(e == -1 for e in temp[a:b]):
                    state[j].pop()
                    cost += 10**i * \
                        (2*ROWS - len(state[j]) - len(state[i]) + b - a)
                    state[i].append(i)
                    check = True

    if all(all(e == i for e in state[i]) and len(state[i]) == ROWS for i in range(4)):
        return cost

    # Check any random moves
    minCost = 10**10
    for i in range(4):
        if all(e == i for e in state[i]):
            continue
        ch = state[i].pop()
        stToMvOut = ROWS - len(state[i])
        c = l = r = 2*i + 2
        while l >= 0:
            if temp[l] != -1:
                break
            if l < 1 or l % 2 == 1:
                temp[l] = ch
                tempCost = 10**ch * (stToMvOut + c - l) + play(state, temp)
                minCost = min(minCost, tempCost)
                temp[l] = -1
            l -= 1
        while r < 11:
            if temp[r] != -1:
                break
            if r > 9 or r % 2 == 1:
                temp[r] = ch
                tempCost = 10**ch * (stToMvOut + r - c) + play(state, temp)
                minCost = min(minCost, tempCost)
                temp[r] = -1
            r += 1
        state[i].append(ch)
    return minCost + cost


ROWS = len(s[0])

print('Part 1:', play(s, temp))

s = [
    [s[0][0], 3, 3, s[0][1]],
    [s[1][0], 1, 2, s[1][1]],
    [s[2][0], 0, 1, s[2][1]],
    [s[3][0], 2, 0, s[3][1]],
]
ROWS = len(s[0])

print('Part 2:', play(s, temp))
