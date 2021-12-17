file_name = 'day9.txt'

with open(file_name) as f:
    map = [[int(a) for a in x] for x in f.read().strip().split('\n')]
x = len(map[0])
y = len(map)


def get_neighbours(i, j):
    U = (i - 1, j) if i > 0 else None
    D = (i + 1, j) if i < y - 1 else None
    L = (i, j - 1) if j > 0 else None
    R = (i, j + 1) if j < x - 1 else None

    return [a for a in [U, D, L, R] if a is not None]


count = 0
low_points = []
for i in range(y):
    for j in range(x):
        if all(map[i][j] < map[n[0]][n[1]] for n in get_neighbours(i, j)):
            low_points.append((i, j))
            count += map[i][j] + 1
print(f'Part 1: {count}')

import queue
basins = {}
for lp in low_points:
    basin = set()
    q = queue.Queue()
    q.put(lp)
    while not q.empty():
        i, j = q.get()
        if not map[i][j] == 9:
            basin.add((i, j))
            points = [n for n in get_neighbours(i, j) if n not in basin]
            for p in points:
                q.put(p)
    basins[lp] = basin
res = sorted([len(b) for b in basins.values()], reverse=True)[0:3]
print(f'Part 2: {res[0]*res[1]*res[2]}')


# from termcolor import colored
# from colorama import init
# init(autoreset=True)
#
# all_basin = [x for b in basins.values() for x in b]
# for i in range(y):
#     for j in range(x):
#         if (i, j) in all_basin:
#             print(colored(map[i][j], 'blue'), end=' ')
#         else:
#             print(map[i][j], end=' ')
#     print('\n', end='')




