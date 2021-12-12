with open('i12.txt') as file:
    m = dict()
    for l in file.readlines():
        a, b = l.strip().split('-')
        m.setdefault(a, []).append(b)
        m.setdefault(b, []).append(a)

stk = []


def dfs(p: str):
    if p == 'end':
        return [1 + len(set(stk)) - len(stk), 1]
    if p.islower():
        if p in stk:
            if len(stk) != len(set(stk)):
                return [0, 0]
        stk.append(p)
    r = [dfs(a) for a in m[p] if a != 'start']
    if p.islower():
        stk.pop()
    return [sum(a for a, _ in r), sum(a for _, a in r)]


print('Part 1: {}\nPart 2: {}'.format(*dfs('start')))
