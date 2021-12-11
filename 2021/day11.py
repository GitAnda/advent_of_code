from termcolor import colored
from colorama import init
import queue
init(autoreset=True)


file_name = 'day11.txt'

with open(file_name) as f:
    list_octos = [[int(x) for x in row] for row in f.read().strip().split('\n')]
x = len(list_octos[0])
y = len(list_octos)

octos = {}
for i, row in enumerate(list_octos):
    for j, o in enumerate(row):
        octos[(i, j)] = list_octos[i][j]


def print_octos(octos):
    for i in range(y):
        for j in range(x):
            v = octos[(i, j)]
            if v == 0:
                print(colored(v, 'yellow'), end=' ')
            else:
                print(v, end=' ')
        print('\n', end='')
    print()


def get_neighbours(i, j):
    U = (i - 1, j) if i > 0 else None
    D = (i + 1, j) if i < y - 1 else None
    L = (i, j - 1) if j > 0 else None
    R = (i, j + 1) if j < x - 1 else None
    UL = (i - 1, j - 1) if i > 0 and j > 0 else None
    DR = (i + 1, j + 1) if i < y - 1 and j < x - 1 else None
    DL = (i + 1, j - 1) if i < y - 1 and j > 0 else None
    UR = (i - 1, j + 1) if i > 0 and j < x - 1 else None
    return [a for a in [U, D, L, R, UL, UR, DL, DR] if a is not None]


def step(octos):
    flashed = set()
    q = queue.Queue()
    for loc in octos.keys():
        octos[loc] += 1
        if octos[loc] == 10:
            flashed.add(loc)
            q.put(loc)

    while not q.empty():
        loc = q.get()
        neighbours = get_neighbours(*loc)
        for loc_n in neighbours:
            octos[loc_n] += 1
            if octos[loc_n] == 10:
                q.put(loc_n)

    count = 0
    for loc in octos.keys():
        if octos[loc] > 9:
            octos[loc] = 0
            count += 1

    return octos, count


res = 0
s = 0
while True:
    octos, dres = step(octos)
    res += dres
    # print_octos(octos)

    if s == 99:
        print(f'Part 1: {res}')
    s += 1

    if dres == x*y:
        print(f'Part 2: {s}')
        break





