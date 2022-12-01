with open('i10.txt') as file:
    data = [list(a.strip()) for a in file.readlines()]

sm = 0
inc = []

op = ['(', '[', '{', '<']
cl = [')', ']', '}', '>']

for d in data:
    st = []
    for c in d:
        if c in op:
            st += [cl[op.index(c)]]
        elif c == st[-1]:
            st.pop()
        else:
            sm += [3, 57, 1197, 25137][cl.index(c)]
            break
    else:
        inc += [int(''.join([str(cl.index(c) + 1) for c in st[::-1]]), 5)]

print('Part 1', sm)
print('Part 2', sorted(inc)[len(inc) // 2])
