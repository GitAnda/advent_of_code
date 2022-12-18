import input
import regex as re
import queue
from itertools import combinations
from collections import defaultdict
from functools import lru_cache

def inf():
    return float('inf')
    
def parse_data():
    r = r'^Valve (.*?) has flow rate=(.*?); tunnel[s]? lead[s]? to valve[s]? (.*?)$'
    lines = [re.findall(r, d)[0] for d in input.retrieve(__file__).split('\n')]
    valves = {a: int(b) for a, b, _ in lines if int(b) != 0 or a == 'AA'}
    # graph = {k: defaultdict(inf) for k in valves}
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
print("Reduced graph build.\n")
# print(REDUCED_GRAPH)

@lru_cache(100000)
def move_and_open_one(opened, time, current):
    if time <= 0 or current in opened:
        return 0
    
    best = 0
    for valve, dist in REDUCED_GRAPH[current].items():
        best = max(best, move_and_open_one((*opened, current), time - dist - 1, valve))
    
    if current == 'AA':
        return best
    return best + time * VALVES[current]

@lru_cache(100000)
def move_and_open_two(opened, time, current):
    if current in opened:
        return 0
    
    if time <= 0:
        return move_and_open_one(opened[1:], 26, 'AA')
    
    best = 0
    for valve, dist in REDUCED_GRAPH[current].items():
        best = max(best, move_and_open_two((*opened, current), time - dist - 1, valve))
    
    if current == 'AA':
        return best
    return best + time * VALVES[current]
            
# res = move_and_open_one((), 30, 'AA')
# print(f"Part 1: {res}")

res = move_and_open_two((), 26, 'AA')
print(f"Part 2: {res}")

