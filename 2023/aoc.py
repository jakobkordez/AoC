from os import path
from random import choice
from typing import Callable, Any
from re import Pattern, match

YEAR = 2023


def _read(s: str, operation: list):
    if not operation:
        return s
    cop, *operation = operation
    if type(cop) is str:
        ts = s.split(cop)
    elif type(cop) is Pattern:
        ts = cop.findall(s)
    else:
        ts = cop(s)
    if operation:
        return [_read(x, operation) for x in ts]
    else:
        return ts


def read(
    name: str | int,
    operations: list[str | Pattern | Callable] = [],
    lstrip: str = "",
    rstrip: str = None,
    download: bool = True,
):
    """
    Reads text file and transforms into specified shape and type

    - `operations`: list of operations to perform on the input
        - `str`: split by `str`
        - `Pattern`: findall by `Pattern`
        - `Callable`: call with input
    - `lstrip`: `str` to lstrip
    - `rstrip`: `str` to rstrip
    - `download`: download input if not found locally
    """

    if type(name) is int:
        name = f"i{name:02d}"
    inpPath = path.join(path.dirname(__file__), f"{name}.txt")

    if download and match(r"^i\d+$", name) and not path.exists(inpPath):
        print("[AoC]: Trying to download input")
        inpData = _downloadInput(int(name[1:]))
        if inpData:
            with open(inpPath, "w") as f:
                f.write(inpData)

    with open(inpPath) as f:
        file = f.read().rstrip(rstrip).lstrip(lstrip)

    return _read(file, operations)


def binarySearch(a: int, b: int, f: Callable[[int], bool]) -> int:
    """
    Binary search for a value in range [a, b)

    - `f`: function that returns `True` if the value is too high
    """

    while a < b:
        m = (a + b) // 2
        if f(m):
            b = m
        else:
            a = m + 1
    return a


def clamp(a: int, x: int, b: int):
    return max(a, min(x, b))


def splitByCount(s: str, c: int):
    return [s[i : i + c] for i in range(0, len(s), c)]


def rollSum(arr: list):
    out = [arr[0]] * len(arr)
    for i in range(1, len(arr)):
        out[i] = out[i - 1] + arr[i]
    return out


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


FOUR_NEIGHBOURS = ((0, -1), (1, 0), (0, 1), (-1, 0))
SIX_NEIGHBOURS = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))
EIGHT_NEIGHBOURS = (*FOUR_NEIGHBOURS, (1, 1), (1, -1), (-1, 1), (-1, -1))


def _downloadInput(day: int):
    import requests

    dirPath = path.dirname(path.dirname(__file__))
    sessionFile = path.join(dirPath, "session.conf")
    if not path.exists(sessionFile):
        print("[AoC]: No session.conf found")
        return

    with open(sessionFile) as f:
        sessionKey = f.read().strip()

    session = requests.Session()
    session.cookies.set("session", sessionKey)
    r = session.get(f"https://adventofcode.com/{YEAR}/day/{day}/input")
    if r.status_code != 200:
        print("[AoC]: Failed to download input", r.status_code)
        return

    return r.text


if __name__ == "__main__":
    import datetime
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", type=int, default=None, required=False)
    args = parser.parse_args()

    if args.d:
        day = args.d
    else:
        day = datetime.datetime.now().day

    pth = path.join(path.dirname(__file__), f"d{day:02d}.py")
    if not path.exists(pth):
        print("[AoC]: Creating new file")
        with open(pth, "w") as f:
            f.write(f"from aoc import *\n\ndata = read({day})")
