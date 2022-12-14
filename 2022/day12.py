import input
import queue
    
def parse_data():
    data = {}
    for i, line in enumerate(input.retrieve(__file__).split('\n')):
        for j, c in enumerate(line):
            ci = ord(c) - 97
            if ci == -14:
                start = (i, j)
                data[(i, j)] = 0
            elif ci == -28:
                end = (i, j)
                data[(i, j)] = 25
            else:
                data[(i, j)] = ci

    return data, start, end

HEIGHTS, START, END = parse_data()
DISTANCE_MATRIX = {START: 0}

def possible_moves(path):
    i, j = path[-1]
    candidates = {(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)}
    neighbours = set()
    for n in candidates:
        i, j = n
        if i >= 0 and j >= 0 and i <= 40 and j <= 153:
            if HEIGHTS[n] <= HEIGHTS[path[-1]] + 1:
                if n not in DISTANCE_MATRIX or (n in DISTANCE_MATRIX and DISTANCE_MATRIX[n] > len(path) + 1):
                    DISTANCE_MATRIX[n] = len(path) + 1
                    neighbours.add(n)
    return neighbours

def search(start):
    q = queue.Queue()
    q.put([start])
    while not q.empty():
        path = q.get()
        candidates = possible_moves(path)
        for loc in candidates:
            q.put(path + [loc])

    return DISTANCE_MATRIX[END] - 1

def search_all():
    for loc, h in HEIGHTS.items():
        if h == 0:
            search(loc)
    return DISTANCE_MATRIX[END] - 1

res = search(START)
print(f"Part 1: {res}")

res = search_all()
print(f"Part 2: {res}")
