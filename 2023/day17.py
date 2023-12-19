import aoc_input
from queue import LifoQueue

day = int(__file__[-5:-3])
GRID = aoc_input.get(day).strip().split("\n")
MAX_I = len(GRID)
MAX_J = len(GRID[0])

def get_all_neighbours(i, j):
    n = []
    if i > 0:
        n.append((i - 1, j))
    if j > 0:
        n.append((i, j - 1))
    if i < MAX_I - 1:
        n.append((i + 1, j))
    if j < MAX_J - 1:
        n.append((i, j + 1))
    return n

def get_valid_neighbours(path, last_dir, count_dir):
    neighbours = get_all_neighbours(*path[-1])

    # Forbidden to go back.
    if path[-2]:
        neighbours.remove(path[-2])

    # Forbidden to go forward more than three squares.
    if count_dir == 3:
        forbidden_pos = (path[-1][0] + last_dir[0], path[-1][1] + last_dir[1])
        if forbidden_pos in neighbours: neighbours.remove(forbidden_pos)
    
    # Return valid neighbours
    return neighbours

def check_bounds(pos, dirc, count_dir, heat_loss):
    bound = BOUNDS[pos][dirc][count_dir] 
    if bound <= heat_loss:
        return False
    
    BOUNDS[pos][dirc][count_dir] = heat_loss
    return True

# BEST = float("inf")
# BOUNDS = {(i, j): {(0, 1): [float("inf")] * 3, (0, -1): [float("inf")] * 3, (1, 0): [float("inf")] * 3, (-1, 0): [float("inf")] * 3} for i in range(MAX_I) for j in range(MAX_J)}

# q = LifoQueue()
# q.put(([None, (0, 0)], None, 0, 0))
# while not q.empty():

#     path, last_dir, count_dir, heat_loss = q.get()
#     next_positions = get_valid_neighbours(path, last_dir, count_dir)

#     for next_pos in next_positions:
#         next_heat_loss = heat_loss + int(GRID[next_pos[0]][next_pos[1]])
#         if next_pos == (MAX_I - 1, MAX_J - 1):
#             if next_heat_loss < BEST:
#                 BEST = next_heat_loss
#             continue

#         next_dir = (next_pos[0] - path[-1][0], next_pos[1] - path[-1][1])

#         if next_dir == last_dir:
#             next_count_dir = count_dir + 1
#         else:
#             next_count_dir = 1
        
#         if BEST < next_heat_loss + MAX_I - next_pos[0] + MAX_J - next_pos[1]:
#             continue

#         if check_bounds(next_pos, next_dir, next_count_dir - 1, next_heat_loss):
#             q.put(([path[-1]] + [next_pos], next_dir, next_count_dir, next_heat_loss))

# print(f"Part 1: {BEST}")

def get_valid_neighbours_two(path, last_dir, count_dir):
    if not last_dir:
        return get_all_neighbours(*path[-1])
    
    neighbours = get_all_neighbours(*path[-1])
    
    # Can only go forward first four steps.
    if count_dir < 4:
        next_pos = (path[-1][0] + last_dir[0], path[-1][1] + last_dir[1])
        if next_pos in neighbours:
            return [next_pos]
        return []
    
    # Forbidden to go back.
    if path[-2]:
        neighbours.remove(path[-2])

    # Forbidden to go forward more than ten squares.
    if count_dir == 10:
        forbidden_pos = (path[-1][0] + last_dir[0], path[-1][1] + last_dir[1])
        if forbidden_pos in neighbours: neighbours.remove(forbidden_pos)
    
    # Return valid neighbours
    return neighbours

def print_path(path):
    for i in range(MAX_I):
        l = ""
        for j in range(MAX_J):
            if (i, j) in path:
                l += "#"
            else:
                l += " "
        print(l)
    print()

# print(get_valid_neighbours_two([None, (0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], (0, 1), 4))
c = 0
BEST = 1003
# BEST = float("inf")
BOUNDS = {(i, j): {(0, 1): [float("inf")] * 7, (0, -1): [float("inf")] * 7, (1, 0): [float("inf")] * 7, (-1, 0): [float("inf")] * 7} for i in range(MAX_I) for j in range(MAX_J)}

q = LifoQueue()
q.put(([None, (0, 0)], None, 0, 0))
while not q.empty():
    if c % 100000 == 0:
        print(f"Queue length {q.qsize()}. Best solution {BEST}.", end="\r")
    c += 1

    path, last_dir, count_dir, heat_loss = q.get()
    # print(path)
    next_positions = get_valid_neighbours_two(path, last_dir, count_dir)
    # print(next_positions)
    for next_pos in next_positions:
        next_heat_loss = heat_loss + int(GRID[next_pos[0]][next_pos[1]])
        next_dir = (next_pos[0] - path[-1][0], next_pos[1] - path[-1][1])

        if next_dir == last_dir:
            next_count_dir = count_dir + 1
        else:
            next_count_dir = 1

        if next_count_dir > 3 and next_pos == (MAX_I - 1, MAX_J - 1):
            if next_heat_loss < BEST:
                # print(next_heat_loss)
                # print_path(path)
                BEST = next_heat_loss
                
            # print("end reached")
            continue
        
        if BEST < next_heat_loss + MAX_I - next_pos[0] + MAX_J - next_pos[1]:
            continue

        if check_bounds(next_pos, next_dir, next_count_dir - 4, next_heat_loss):
            # q.put(([path[-1]] + [next_pos], next_dir, next_count_dir, next_heat_loss))
            q.put((path + [next_pos], next_dir, next_count_dir, next_heat_loss))

print(f"Part 2: {BEST}                           ")


