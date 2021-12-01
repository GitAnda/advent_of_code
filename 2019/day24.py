layout = {}
f = open('day24.txt', 'r')
for i, line in enumerate(f.read().split('\n')):
    for j, tile in enumerate(line):
        layout[(i, j)] = tile
f.close()

def print_layout(l):
    for i in range(5):
        for j in range(5):
            print(l[(i, j)], end=' ')
        print()
    print()

print_layout(layout)

def make_string(l):
    s = ''
    for i in range(5):
        for j in range(5):
            s += l[(i, j)]
    return s

def time_step(l):
    new_layout = {}
    for i in range(5):
        for j in range(5):
            neighbour_bugs = 0
            if i+1 < 5 and l[(i+1, j)] == '#':
                neighbour_bugs += 1
            if i-1 >= 0 and l[(i-1, j)] == '#':
                neighbour_bugs += 1
            if j+1 < 5 and l[(i, j+1)] == '#':
                neighbour_bugs += 1
            if j-1 >= 0 and l[(i, j-1)] == '#':
                neighbour_bugs += 1

            if l[(i, j)] == '#':
                if neighbour_bugs == 1:
                    new_layout[(i, j)] = '#'
                else:
                    new_layout[(i, j)] = '.'
            else:
                if 1 <= neighbour_bugs < 3:
                    new_layout[(i, j)] = '#'
                else:
                    new_layout[(i, j)] = '.'

    return new_layout

layout_log = []
string_layout = make_string(layout)
while string_layout not in layout_log:
    layout_log.append(string_layout)
    layout = time_step(layout)
    string_layout = make_string(layout)
    # print_layout(layout)

def biodiversity(string_layout):
    b = 0
    for i, c in enumerate(string_layout):
        if c == '#':
            b += pow(2, i)
    return b

print_layout(layout)
print(biodiversity(string_layout))


