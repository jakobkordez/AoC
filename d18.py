with open('i18.txt') as file:
    data = []
    for l in file.readlines():
        c = 0
        ll = []
        for ch in l.strip():
            if ch == '[':
                c += 1
            elif ch == ']':
                c -= 1
            elif ch >= '0' and ch <= '9':
                ll.append((int(ch), c))
        data.append(ll)


def reduce(st):
    i = 0
    while i < len(st):
        while i + 1 < len(st):
            a, d = st[i]
            b, e = st[i+1]
            if d > 4 and d == e:
                if i > 0:
                    st[i - 1] = st[i-1][0] + a, st[i-1][1]
                if i + 2 < len(st):
                    st[i + 2] = st[i+2][0] + b, st[i+2][1]
                st.pop(i)
                st[i] = 0, d - 1
                i = 0
            else:
                i += 1
        i = 0
        while i < len(st):
            a, d = st[i]
            if a >= 10:
                st[i] = (a + 1) // 2, d + 1
                st.insert(i, (a//2, d+1))
                i = 0
                break
            else:
                i += 1
    return st


def getMag(st):
    while len(st) != 1:
        i = 0
        while i + 1 < len(st):
            a, d = st[i]
            b, e = st[i+1]
            if d == e:
                st.pop(i)
                st[i] = 3*a + 2*b, d-1
                i = 0
            else:
                i += 1
    return st[0][0]


st = list(data[0])
for ss in data[1:]:
    st = reduce([(a, b+1) for a, b in st] + [(a, b+1) for a, b in ss])

print('Part 1:', getMag(st))

mxmag = 0
for ii in range(len(data)):
    for jj in range(len(data)):
        if ii == jj:
            continue
        st = reduce([(a, b+1) for a, b in data[ii]] + [(a, b+1)
                    for a, b in data[jj]])
        mxmag = max(mxmag, getMag(st))

print('Part 2:', mxmag)
