import re
import numpy as np

with open('i4.txt') as file:
    raw = file.read().split('\n\n')

nums = np.array(list(map(int, raw[0].split(','))))
boards = [np.array([list(map(int, (re.split(r'\s+', row.strip())))) for row in b.split('\n')])
          for b in raw[1:]]

score = None
wb = [False] * len(boards)
for i in range(5, len(nums)):
    for bi in range(len(boards)):
        if wb[bi]:
            continue
        b = boards[bi]
        for j in range(5):
            if np.all(np.isin(b[j], nums[:i])) or np.all(np.isin(b[:, j], nums[:i])):
                tscore = (sum(b.flatten()) -
                          sum(np.intersect1d(b.flatten(), nums[:i]))) * nums[i - 1]
                wb[bi] = True
                if score == None:
                    print('Part 1:', tscore)
                score = tscore

print('Part 2:', score)
