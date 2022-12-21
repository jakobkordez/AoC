from os import path
from random import choice
from typing import Callable, Any
from re import Pattern


def _read(s: str, operation: list, typ: type):
    if operation:
        cop, *operation = operation
        if type(cop) is str:
            ts = s.split(cop)
        elif type(cop) is Pattern:
            ts = cop.findall(s)
        else:
            ts = cop(s)
        return [_read(x, operation, typ) for x in ts]
    else:
        return typ(s)


def read(name: str, operations: list = [], typ: type = str, lstrip: str = '', rstrip: str = None):
    """
    Reads text file and transforms into specified shape and type

    `operations`: list of operations to perform on the input
        `str`: split by `str`
        `Pattern`: findall by `Pattern`
        `Callable`: call with input
    `typ`: type to cast to
    `lstrip`: `str` to lstrip
    `rstrip`: `str` to rstrip
    """

    inpPath = path.join(path.dirname(__file__), f'{name}.txt')

    with open(inpPath) as f:
        file = f.read().rstrip(rstrip).lstrip(lstrip)

    return _read(file, operations, typ)


def clamp(a: int, x: int, b: int):
    return max(a, min(x, b))


def splitByCount(s: str, c: int):
    return [s[i:i+c] for i in range(0, len(s), c)]


def qsorted(arr: list, cmp: Callable[[Any, Any], int]) -> list:
    """
    Quick sort list with a custom comparator

    Returns a new list
    """

    if len(arr) <= 1:
        return arr
    pivot = choice(arr)
    left = []
    middle = []
    right = []
    for x in arr:
        cv = cmp(x, pivot)
        if cv < 0:
            left.append(x)
        elif cv == 0:
            middle.append(x)
        else:
            right.append(x)
    return qsorted(left, cmp) + middle + qsorted(right, cmp)


FOUR_NEIGHBOURS = ((0, 1), (0, -1), (1, 0), (-1, 0))
SIX_NEIGHBOURS = ((0, 0, 1), (0, 0, -1), (0, 1, 0),
                  (0, -1, 0), (1, 0, 0), (-1, 0, 0))
EIGHT_NEIGHBOURS = (*FOUR_NEIGHBOURS, (1, 1), (1, -1), (-1, 1), (-1, -1))
