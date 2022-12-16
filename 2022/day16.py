import input
import regex as re
import queue
from itertools import combinations
    
def parse_data():
    r = r'^Valve (.*?) has flow rate=(.*?); tunnel[s]? lead[s]? to valve[s]? (.*?)$'
    valves = {a: int(b) for d in input.retrieve(__file__).split('\n') for a, b, _ in re.findall(r, d) if int(b) != 0}
    graph = {a: set(c.split(', ')) for d in input.retrieve(__file__).split('\n') for a, _, c in re.findall(r, d)}
    return valves, graph

VALVES, GRAPH = parse_data()
REDUCED_GRAPH = {v: {k: float('inf') for k in VALVES if k != v} for v in VALVES}
START = {v: float('inf') for v in VALVES}

def move_step(path):
    valve = path[-1]
    children = [next_valve for next_valve in GRAPH[valve]if next_valve not in path]
    return children

def get_start_distance():
    path = ['AA']
    q = queue.Queue()
    q.put(path)
    
    while not q.empty():
        path = q.get()
        children = move_step(path)
        for child in children:
            if child in VALVES and len(path) < START[child]:
                START[child] = len(path)
            q.put(path + [child])

get_start_distance()

def reduce_graph():
    for valve in VALVES:
        path = [valve]
        q = queue.Queue()
        q.put(path)
        
        while not q.empty():
            path = q.get()
            children = move_step(path)
            for child in children:
                if child in VALVES and len(path) < REDUCED_GRAPH[path[0]][child]:
                    REDUCED_GRAPH[path[0]][child] = len(path)
                q.put(path + [child])

reduce_graph()
print(REDUCED_GRAPH)
print("Reduced graph build.\n")

def move_and_open(node):
    pres, time, path = node
    children = []
    for next_loc in VALVES:
        if next_loc not in path:
            new_time = time - REDUCED_GRAPH[path[-1]][next_loc] - 1
            if new_time > 0:
                children.append((pres + new_time * VALVES[next_loc], new_time, path + [next_loc]))
    return children

def release_pressure():
    q = queue.Queue()
    for start in START:
        time_left = 30 - START[start] - 1
        q.put((time_left * VALVES[start], time_left, [start]))
    res = 0
    the_path = []
    
    while not q.empty():
        node = q.get()
        children = move_and_open(node)
        
        for child in children:
            pres = child[0]
            if res < pres:
                res = pres
                the_path = child[2]
                
            q.put(child)
            
            
    print(the_path)     
    return res

def release_pressure_greedy():
    
    max_pres_time = 0
    for start in START:
        time = START[start] + 1
        if 30 - time > 0:
            pres = (30 - time) * VALVES[start]
            if pres / time > max_pres_time:
                max_pres_time = pres / time
                next_pres, start_loc, next_time = (pres, start, 30 - time)
    total_pres, path, total_time = (next_pres, [start_loc], 30 - time)
    
    while True:
        print('-----', total_pres, path, total_time)
        old_pres = total_pres
        max_pres_time = 0
        next_pres = 0
        for next_loc in VALVES:
            if next_loc not in path:
                time = REDUCED_GRAPH[path[-1]][next_loc] - 1
                print(next_loc, total_time - time)
                if total_time - time > 0:
                    pres = (total_time - time) * VALVES[next_loc]
                    # print(pres)
                    if pres / time > max_pres_time:
                        max_pres_time = pres / time
                        next_pres, next_path, next_time = (pres, next_loc, time)
        total_pres, path, total_time = (total_pres + next_pres, path + [next_path], total_time - next_time)
        
        if old_pres == total_pres:
            break
        
    print(path)             
    return total_pres

def move_and_open_pair(node):
    pres, (time1, time2), (path1, path2) = node
    
    children = []
    comb = combinations([v for v in VALVES if v not in path1 and v not in path2], 2)
    
    for loc1, loc2 in comb:
        new_time_1 = time1 - REDUCED_GRAPH[path1[-1]][loc1] - 1
        new_time_2 = time2 - REDUCED_GRAPH[path2[-1]][loc2] - 1
        
        if new_time_1 > 0 and new_time_2 > 0:
            new_pres = pres + new_time_1 * VALVES[loc1] + new_time_2 * VALVES[loc2]
            children.append((new_pres, (new_time_1, new_time_2), (path1 + [loc1], path2 + [loc2])))
        elif new_time_1 > 0:
            new_pres = pres + new_time_1 * VALVES[loc1]
            children.append((new_pres, (new_time_1, time2), (path1 + [loc1], path2)))
        elif new_time_2 > 0:
            new_pres = pres + new_time_2 * VALVES[loc2]
            children.append((new_pres, (time1, new_time_2), (path1, path2 + [loc2])))
            
    return children

def release_pressure_pair():
    q = queue.Queue()
    comb = combinations([v for v in VALVES], 2)
    for start1, start2 in comb:
        time1 = 26 - START[start1] - 1
        time2 = 26 - START[start2] - 1
        pres = time1 * VALVES[start1] + time2 * VALVES[start2]
        q.put((pres, (time1, time2), ([start1], [start2])))
        
    res = 0
    count = 0
    while not q.empty():
    # for _ in range(10):
        count += 1
        if count % 10000 == 0:
            print(count, len(q.queue), end='\r')
        node = q.get()
        children = move_and_open_pair(node)
        # print(node, children)
        
        for child in children:
            pres = child[0]
            if res < pres:
                res = pres
                
            q.put(child)
                    
    return res
            
res = release_pressure_greedy()
res = release_pressure()
print(f"Part 1: {res}")

# res = release_pressure_pair()
# print(f"Part 2: {res}")
