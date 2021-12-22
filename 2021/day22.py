file_name = 'day22.txt'
with open(file_name) as f:
    operations = [[x.split(' ')[0], [sorted([int(z) for z in y[2:].split('..')]) for y in x.split(' ')[1].split(',')]] for x in f.read().strip().split('\n')]

cubes_on = []
for i, (switch, (x, y, z)) in enumerate(operations):
    new_cubes_on = []

    for xo, yo, zo in cubes_on:
        if xo[0] > x[1] or x[0] > xo[1] or yo[0] > y[1] or y[0] > yo[1] or zo[0] > z[1] or z[0] > zo[1]:
            new_cubes_on.append([xo, yo, zo])
        else:
            if x[0] - xo[0] > 0:
                new_cubes_on.append([[xo[0], x[0] - 1], list(yo), list(zo)])
                xo[0] = x[0]
            if xo[1] - x[1] > 0:
                new_cubes_on.append([[x[1] + 1, xo[1]], list(yo), list(zo)])
                xo[1] = x[1]

            if y[0] - yo[0] > 0:
                new_cubes_on.append([list(xo), [yo[0], y[0] - 1], list(zo)])
                yo[0] = y[0]
            if yo[1] - y[1] > 0:
                new_cubes_on.append([list(xo), [y[1] + 1, yo[1]], list(zo)])
                yo[1] = y[1]

            if z[0] - zo[0] > 0:
                new_cubes_on.append([list(xo), list(yo), [zo[0], z[0] - 1]])
                # zo[0] = z[0]
            if zo[1] - z[1] > 0:
                new_cubes_on.append([list(xo), list(yo), [z[1] + 1, zo[1]]])
                # zo[1] = z[1]

    if switch == 'on':
        new_cubes_on.append([list(x), list(y), list(z)])
    cubes_on = new_cubes_on

    if i == 19:
        count = 0
        for x, y, z in cubes_on:
            count += (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)
        print(f'Part 1: {count}')


count = 0
for x, y, z in cubes_on:
    count += (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)
print(f'Part 2: {count}')



