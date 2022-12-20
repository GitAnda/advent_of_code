import regex as re
import queue
from functools import lru_cache

def parse_data():
    r = r'^Valve (.*?) has flow rate=(.*?); tunnel[s]? lead[s]? to valve[s]? (.*?)$'
    lines = [re.findall(r, d)[0] for d in input.retrieve(__file__).split('\n')]
    valves = {a: int(b) for a, b, _ in lines if int(b) != 0 or a == 'AA'}
    graph = {a: {k: 1 for k in c.split(', ')} for a, _, c in lines}
    return valves, graph

VALVES, GRAPH = parse_data()

def reduce_graph():
    valves_and_start = list(VALVES.keys()) + ['AA']
    reduced_graph = {v: {k: float('inf') for k in VALVES if k != v} for v in valves_and_start}
    
    for valve in valves_and_start:
        path = [valve]
        q = queue.Queue()
        q.put(path)
        
        while not q.empty():
            path = q.get()
            valve = path[-1]
            children = [next_valve for next_valve in GRAPH[valve] if next_valve not in path]
            for child in children:
                if child in VALVES and len(path) < reduced_graph[path[0]][child]:
                    reduced_graph[path[0]][child] = len(path)
                q.put(path + [child])
                
    return reduced_graph

REDUCED_GRAPH = reduce_graph()

@lru_cache(100000)
def move_and_open(opened, time, current):
    if time <= 0 or current in opened:
        return (0, ())
    
    best = [(0, ())]
    for valve, dist in REDUCED_GRAPH[current].items():
        best.append(move_and_open((*opened, current), time - dist - 1, valve))
    best_res, best_opened = max(best)
    
    if current == 'AA':
        return best_res, best_opened
    return best_res + time * VALVES[current], (*best_opened, current)
            
res, _ = move_and_open((), 30, 'AA')
print(f"Part 1: {res}")

res_olly, opened_olly = move_and_open((), 26, 'AA')
res_me, _ = move_and_open(opened_olly, 26, 'AA')
print(f"Part 2: {res_olly + res_me}")

