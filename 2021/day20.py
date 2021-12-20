file_name = 'day20.txt'
with open(file_name) as f:
    algorithm, image = f.read().strip().split('\n\n')
image = [x for x in image.split('\n')]

light_spots = set()
for i in range(len(image)):
    for j in range(len(image[0])):
        if image[i][j] == '#':
            light_spots.add((i, j))

min_i, max_i = 0, len(image)
min_j, max_j = 0, len(image[0])
limits = (min_i, max_i, min_j, max_j)


def read_grid(spots, i, j, limits, beyond):
    grid = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    min_i, max_i, min_j, max_j = limits
    digit = []
    for g in grid:
        if min_i <= g[0] < max_i and min_j <= g[1] < max_j:
            if g in spots:
                digit.append('#')
            else:
                digit.append('.')
        else:
            digit.append(beyond)
    digit = ''.join(digit).replace('#', '1').replace('.', '0')
    return int(digit, 2)


def step(spots, limits, beyond):
    min_i, max_i, min_j, max_j = limits

    new_spots = set()
    for a in range(min_i-1, max_i+1):
        for b in range(min_j-1, max_j+1):
            d = read_grid(spots, a, b, limits, beyond)
            if algorithm[d] == '#':
                new_spots.add((a, b))

    min_i, max_i = min_i - 1, max_i + 1
    min_j, max_j = min_j - 1, max_j + 1
    return new_spots, (min_i, max_i, min_j, max_j)


def print_spots(spots, limits):
    min_i, max_i, min_j, max_j = limits
    for a in range(min_i, max_i):
        for b in range(min_j, max_j):
            if (a, b) in spots:
                print('#', end='')
            else:
                print('.', end='')
        print(' ', end='\n')
    print()



if algorithm[0] == '.':
    out_of_scope = ['0', '0']
else:
    out_of_scope = ['0', '1']

# print_spots(light_spots, limits)
for t in range(50):
    light_spots, limits = step(light_spots, limits, out_of_scope[t%2])
    # print_spots(light_spots, limits)
    if t == 1:
        print(f'Part 1: {len(light_spots)}')
print(f'Part 2: {len(light_spots)}')








