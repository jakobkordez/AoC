def _read(s: str, dellimiters: list, typ: type):
    if dellimiters:
        cd, *dellimiters = dellimiters
        return [_read(x, dellimiters, typ) for x in s.split(cd)]
    else:
        return typ(s)


def read(name: str, dellimiters: list = [], typ: type = str):
    with open(f'{name}.txt') as f:
        file = f.read().rstrip()
    return _read(file, dellimiters, typ)