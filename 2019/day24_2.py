initial_layout = {}
f = open('day24.txt', 'r')
for i, line in enumerate(f.read().split('\n')):
    for j, tile in enumerate(line):
        initial_layout[(i-2, j-2)] = tile
f.close()

initial_layout[(0, 0)] = '?'
total_layout = {0: initial_layout}

def print_layout(l):
    depths = sorted(l.keys())
    for depth in depths:
        print(f'Depth  {depth}:')
        l_depth = l[depth]
        for i in range(5):
            for j in range(5):
                print(l_depth[(i-2, j-2)], end=' ')
            print()
        print()

print_layout(total_layout)

new_layer = {}
for i in range(5):
    for j in range(5):
        new_layer[(i-2, j-2)] = '.'
new_layer[(0, 0)] = '?'

def time_step(ti, l):
    new_l = {}
    depths = sorted(l.keys())
    for depth in depths:
        new_l_depth = {}
        for i in range(5):
            i -= 2
            for j in range(5):
                j -= 2

                # if depth is not 0 and (abs(depth) - 1) * 2 + abs(i) + abs(j) > ti + 1:
                #     new_l_depth[(i, j)] = '.'
                #     continue

                if i == 0 and j == 0:
                    new_l_depth[(i, j)] = '?'
                    continue

                n = [(i, j+1), (i+1, j), (i, j-1), (i-1, j)]
                neighbours = []
                bugs = 0

                for (xi, yi) in n:
                    if abs(xi) > 2 or abs(yi) > 2:
                        neighbours.append((depth-1, int(xi/3), int(yi/3)))
                    elif xi == 0 and yi == 0:
                        for f in list(range(-2, 3)):
                            neighbours.append((depth+1, i*2 + (0==i)*f, j*2 + (0==j)*f))
                    else:
                        neighbours.append((depth, xi, yi))

                # print(f'Neigbours of {(depth, i, j)} are {neighbours}')

                for d, xi, yi in neighbours:
                    if d in l.keys():
                        if l[d][(xi, yi)] == '#':
                            bugs += 1

                if l[depth][(i, j)] == '#':
                    if bugs == 1:
                        new_l_depth[(i, j)] = '#'
                    else:
                        new_l_depth[(i, j)] = '.'
                else:
                    if 1 <= bugs < 3:
                        new_l_depth[(i, j)] = '#'
                    else:
                        new_l_depth[(i, j)] = '.'

        new_l[depth] = new_l_depth

    return new_l

for t in range(200):
    depth = max(total_layout.keys()) + 1
    if t % 2 == 0:
        total_layout[depth] = new_layer
        total_layout[-depth] = new_layer
    total_layout = time_step(t, total_layout)

# print_layout(total_layout)

bug_count = 0
for depth, layout in total_layout.items():
    for tile in layout.values():
        if tile == '#':
            bug_count += 1

print(bug_count)






