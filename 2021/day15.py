import queue

file_name = 'day15.txt'
with open(file_name) as f:
    cave = [[int(x) for x in line] for line in f.read().strip().split('\n')]
x = len(cave[0])
y = len(cave)


def get_neighbours(i, j):
    D = (i + 1, j) if i < Y - 1 else None
    R = (i, j + 1) if j < X - 1 else None
    U = (i - 1, j) if i > 0 else None
    L = (i, j - 1) if j > 0 else None
    return [a for a in [D, R, U, L] if a is not None]


cave_map = {}
for i in range(x):
    for j in range(y):
        for a in range(5):
            for b in range(5):
                c = cave[i][j] + a + b
                cave_map[(i+a*x, j+b*y)] = c if c < 10 else c - 9
X = 5*x
Y = 5*y

risk_matrix = {(0, 0): 0}
q = queue.PriorityQueue()
q.put((0, (0, 0)))
while not q.empty():
    risk, loc = q.get()
    neighbours = get_neighbours(*loc)
    for n in neighbours:
        r = cave_map[n]
        if n not in risk_matrix.keys() or risk_matrix[n] > r + risk:
            risk_matrix[n] = r + risk
            q.put((r + risk, n))

print(f'Part 1: {risk_matrix[(x-1, y-1)]}')
print(f'Part 2: {risk_matrix[(X-1, Y-1)]}')
