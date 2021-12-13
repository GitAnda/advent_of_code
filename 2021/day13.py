import numpy as np

file_name = 'day13.txt'
with open(file_name) as f:
    locs, folds = f.read().strip().split('\n\n')

locs = set([tuple([int(x) for x in l.split(',')]) for l in locs.split('\n')])
folds = [(fold.split('=')[0][-1], int(fold.split('=')[1])) for fold in folds.split('\n')]


def fold(axis, number, dots):
    new_dots = set()
    for x, y in dots:
        if axis == 'x':
            if x > number:
                new_dots.add((2 * number - x, y))
            elif x < number:
                new_dots.add((x, y))
        elif axis == 'y':
            if y > number:
                new_dots.add((x, 2 * number - y))
            elif y < number:
                new_dots.add((x, y))
    return new_dots


def print_paper(dots):
    max_x = -np.inf
    min_x = np.inf
    min_y = np.inf
    max_y = -np.inf
    for x, y in dots:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in dots:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print('\n', end='')
    print()


for i, f in enumerate(folds):
    a, n = f
    locs = fold(a, n, locs)
    if i == 0:
        print(f'Part 1: {len(locs)}')
print('Part 2:')
print_paper(locs)
