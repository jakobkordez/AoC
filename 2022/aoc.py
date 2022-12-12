from os import path


def _read(s: str, dellimiters: list, typ: type):
    if dellimiters:
        cd, *dellimiters = dellimiters
        s = s.split(cd) if type(cd) is str else cd(s)
        return [_read(x, dellimiters, typ) for x in s]
    else:
        return typ(s)


def read(name: str, dellimiters: list = [], typ: type = str, lstrip: str = '', rstrip: str = None):
    inpPath = path.join(path.dirname(__file__), f'{name}.txt')

    with open(inpPath) as f:
        file = f.read().rstrip(rstrip).lstrip(lstrip)

    return _read(file, dellimiters, typ)


def clamp(a: int, x: int, b: int):
    return max(a, min(x, b))


def splitByCount(s: str, c: int):
    return [s[i:i+c] for i in range(0, len(s), c)]


FOUR_NEIGHBOURS = ((0, 1), (0, -1), (1, 0), (-1, 0))
EIGHT_NEIGHBOURS = (*FOUR_NEIGHBOURS, (1, 1), (1, -1), (-1, 1), (-1, -1))
