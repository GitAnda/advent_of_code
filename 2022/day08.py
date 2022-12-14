import input
    
def parse_data():
    data = [[int(t) for t in row] for row in input.retrieve(__file__).split('\n')]
    return data

data = parse_data()

def list_visible(line, reversed=False):
    max_height = -1
    count = []
    for i, tree in enumerate(line):
        if tree > max_height:
            count.append(i) if not reversed else count.append(len(line) - i - 1)
            max_height = tree
    return count 

def count_visible(data):
    visible = []
    for i, row in enumerate(data):
        visible += [(i, j) for j in list_visible(row)]
        visible += [(i, j) for j in list_visible(list(reversed(row)), True)]
    for j, column in enumerate(zip(*data)):
        visible += [(i, j) for i in list_visible(column)]
        visible += [(i, j) for i in list_visible(list(reversed(column)), True)]   
    return len(set(visible))

def count_view(line, max_height, rev=False):
    count = 0
    if rev:
        line = list(reversed(line))
    for tree in line:
        if tree < max_height:
            count += 1
        else:
            count += 1
            break
    return count 

def calculate_scenic(data, loc):
    i, j = loc
    row = data[i]
    column = list(zip(*data))[j]
    height = data[i][j]
    
    a = count_view(row[j+1:], height)
    b = count_view(row[:j], height, True)
    c = count_view(column[i+1:], height)
    d = count_view(column[:i], height, True)
    
    return a * b * c * d

res = count_visible(data)
print(f"Part 1: {res}")

res = max([calculate_scenic(data, (i, j)) for i in range(len(data)) for j in range(len(list(zip(*data))))])
print(f"Part 2: {res}")
