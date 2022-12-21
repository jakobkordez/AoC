from aoc import *

origCoords = read('i20', ['\n'], int)
N = len(origCoords)


class Node:
    def __init__(self, val):
        self.val = val
        self.prev: Node = None
        self.next: Node = None

    def nextN(self, n):
        curr = self
        for _ in range(n):
            curr = curr.next
        return curr

    def prevN(self, n):
        curr = self
        for _ in range(n):
            curr = curr.prev
        return curr


def solve(decrKey, rounds):
    coords = [Node(x * decrKey) for x in origCoords]
    for i in range(N):
        coords[i].prev = coords[(i - 1) % N]
        coords[i].next = coords[(i + 1) % N]

    for _ in range(rounds):
        for curr in coords:
            # Remove curr
            pr = curr.prev
            nx = curr.next
            pr.next = nx
            nx.prev = pr

            # Find destination
            val = abs(curr.val) % (N - 1)
            if curr.val > 0:
                nx = nx.nextN(val)
            else:
                nx = nx.prevN(val)
            pr = nx.prev

            # Insert curr
            nx.prev = curr
            curr.next = nx
            curr.prev = pr
            pr.next = curr

    sol = 0
    for curr in coords:
        if curr.val == 0:
            break
    for _ in range(3):
        curr = curr.nextN(1000 % N)
        sol += curr.val
    return sol


print('Part 1:', solve(1, 1))
print('Part 2:', solve(811589153, 10))
