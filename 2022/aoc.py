from os import path


def _read(s: str, dellimiters: list, typ: type):
    if dellimiters:
        cd, *dellimiters = dellimiters
        return [_read(x, dellimiters, typ) for x in s.split(cd)]
    else:
        return typ(s)


def read(name: str, dellimiters: list = [], typ: type = str, lstrip: str = '', rstrip: str = None):
    inpPath = path.join(path.dirname(__file__), f'{name}.txt')

    with open(inpPath) as f:
        file = f.read().rstrip(rstrip).lstrip(lstrip)

    return _read(file, dellimiters, typ)
