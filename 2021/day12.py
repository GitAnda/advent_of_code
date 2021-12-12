import queue

file_name = 'day12.txt'

with open(file_name) as f:
    edges = [e.split('-') for e in f.read().strip().split('\n')]

graph = {}
for s, e in edges:
    if s in graph.keys():
        graph[s].append(e)
    else:
        graph[s] = [e]

    if e in graph.keys():
        graph[e].append(s)
    else:
        graph[e] = [s]

q = queue.Queue()
q.put(['start'])
count = 0
while not q.empty():
    path = q.get()
    next_caves = graph[path[-1]]
    for n in next_caves:
        if n == 'end':
            count += 1
        elif n.isupper() or n not in path:
            q.put(path + [n])
print(f'Part 1: {count}')

q = queue.Queue()
q.put(['start'])
count = 0
while not q.empty():
    path = q.get()
    next_caves = graph[path[-1]]
    for n in next_caves:
        if n == 'end':
            # print(path+[n])
            count += 1
        elif n.isupper() or n not in path:
            q.put(path + [n])
        else:
            if not n == 'start' and not any([path.count(p) > 1 for p in path if p.islower()]):
                q.put(path + [n])
print(f'Part 2: {count}')