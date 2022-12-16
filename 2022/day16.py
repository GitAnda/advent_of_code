import regex as re
import queue
from itertools import combinations


def parse_data():
    r = r'^Valve (.*?) has flow rate=(.*?); tunnel[s]? lead[s]? to valve[s]? (.*?)$'
    valves = {a: int(b) for d in open("2022\day16.txt").readlines() for a, b, _ in re.findall(r, d) if int(b) != 0}
    graph = {a: set(c.split(', ')) for d in open("2022\day16.txt").readlines() for a, _, c in re.findall(r, d)}
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
# print(START)


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
# print(REDUCED_GRAPH)
print("Reduced graph build.\n")


def next_best_move(path, total_time):
    # print(path, total_time)
    max_pres_time = 0
    for next_loc in VALVES:
        if next_loc not in path:
            time = REDUCED_GRAPH[path[-1]][next_loc] + 1
            if total_time - time > 0:
                pres = (total_time - time) * VALVES[next_loc]
                # print(next_loc, pres, time, pres / time)
                if pres / time > max_pres_time:
                    max_pres_time = pres / time
                    out = (pres, next_loc, time, pres / time)
    
    if max_pres_time:
        return out

def calc_pressure(path, start_time):
    pres = 0
    time = START[path[0]] + 1
    pres += (start_time - time) * VALVES[path[0]]
    start_time -= time

    for i in range(1, len(path)):
        time = REDUCED_GRAPH[path[i - 1]][path[i]] + 1
        pres += (start_time - time) * VALVES[path[i]]
        start_time -= time

    return pres


print(calc_pressure(['DD', 'BB', 'JJ', 'HH', 'EE', 'CC'], 30))


def release_pressure():
    max_pres_time = 0
    for start in START:
        time = START[start] + 1
        if 30 - time > 0:
            pres = (30 - time) * VALVES[start]
            if pres / time > max_pres_time:
                max_pres_time = pres / time
                next_pres, start_loc, next_time = (pres, start, 30 - time)
    total_pres, path, total_time = (next_pres, [start_loc], next_time)
    # print(total_pres, path, total_time)
    
    while True:
        best_move = next_best_move(path, total_time)
        # print(path, best_move)
        if best_move:
            next_pres, next_path, next_time, _ = best_move
            total_pres, path, total_time = (total_pres + next_pres, path + [next_path], total_time - next_time)
        else:
            break

    print(path)
                  
    return total_pres


# def release_pressure_pair():
#     pres_time = []
#     for start in START:
#         time = START[start] + 1
#         if 26 - time > 0:
#             pres = (26 - time) * VALVES[start]
#             pres_time.append((pres / time, pres, [start], 26 - time))

#     pres_time.sort(reverse=True)
#     print(pres_time)
#     pres1, path1, time1 = tuple(pres_time[0][1:])
#     pres2, path2, time2 = tuple(pres_time[1][1:])
    
#     # while True:
#     for _ in range(10):

#         best_move_1 = next_best_move(path2 + path1, time1)
#         best_move_2 = next_best_move(path1 + path2, time2)

#         print(path1, path2)
#         print(best_move_1, best_move_2)
        

#         if not best_move_1 and not best_move_2:
#             print(pres1 , pres2, path1, path2, time1, time2)
#             return pres1 + pres2

#         elif best_move_1 and not best_move_2:
#             next_pres1, next_path1, next_time1, _ = best_move_1
#             pres1, path1, time1 = (pres1 + next_pres1, path1 + [next_path1], time1 - next_time1)

#         elif best_move_2 and not best_move_1:
#             next_pres2, next_path2, next_time2, _ = best_move_2
#             pres2, path2, time2 = (pres2 + next_pres2, path2 + [next_path2], time2 - next_time2)

#         else:
#             next_pres1, next_path1, next_time1, pres_time1 = best_move_1
#             next_pres2, next_path2, next_time2, pres_time2 = best_move_2
#             if next_path1 == next_path2:
#                 if pres_time1 >= pres_time2:
#                     pres1, path1, time1 = (pres1 + next_pres1, path1 + [next_path1], time1 - next_time1)
#                     best_move_2 = next_best_move(path1 + path2, time2)
#                     next_pres2, next_path2, next_time2, _ = best_move_2
#                     pres2, path2, time2 = (pres2 + next_pres2, path2 + [next_path2], time2 - next_time2)
#                 else:
#                     pres2, path2, time2 = (pres2 + next_pres2, path2 + [next_path2], time2 - next_time2)
#                     best_move_1 = next_best_move(path2 + path1, time1)
#                     next_pres1, next_path1, next_time1, _ = best_move_1
#                     pres1, path1, time1 = (pres1 + next_pres1, path1 + [next_path1], time1 - next_time1)
#             else:
#                 next_pres1, next_path1, next_time1, _ = best_move_1
#                 pres1, path1, time1 = (pres1 + next_pres1, path1 + [next_path1], time1 - next_time1)
#                 next_pres2, next_path2, next_time2, _ = best_move_2
#                 pres2, path2, time2 = (pres2 + next_pres2, path2 + [next_path2], time2 - next_time2)
        
        

            
res = release_pressure()
print(f"Part 1: {res}")


# res = release_pressure_pair()
# print(f"Part 2: {res}")
