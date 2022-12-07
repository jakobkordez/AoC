from aoc import *
from bisect import bisect_right

cmds = read('i07', ['\n$ ', '\n', ' '], lstrip='$ ')

curr = root = {'d': {}, 'f': 0, 'p': None}

for (cmd, *args), *res in cmds:
    match cmd:
        case 'cd':
            match args[0]:
                case '/': curr = root
                case '..': curr = curr['p']
                case _: curr = curr['d'][args[0]]
        case 'ls':
            for size, name in res:
                match size:
                    case 'dir': curr['d'][name] = {'d': {}, 'f': 0, 'p': curr}
                    case _: curr['f'] += int(size)


dirs = []


def dfs(node):
    size = sum(map(dfs, node['d'].values())) + node['f']
    dirs.append(size)
    return size


requiredSpace = dfs(root) - 40000000
dirs.sort()

print('Part 1:', sum(dirs[:bisect_right(dirs, 100000)]))
print('Part 2:', dirs[bisect_right(dirs, requiredSpace)])
