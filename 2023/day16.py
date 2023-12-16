import aoc_input
from functools import lru_cache
from tqdm import tqdm
from queue import Queue

day = int(__file__[-5:-3])
GRID = aoc_input.get(day).strip().split("\n")
DIR = {0: "N", 1: "E", 2: "S", 3: "W"} #"N": 0, "E": 1, "S": 2, "W": 3, 

@lru_cache(maxsize=None)
def get_next_position(i, j, direction):
    match direction:
        case 0:
            if i > 0:
                return (i - 1, j)
        case 1:
            if j < len(GRID[0]) - 1:
                return (i, j + 1)   
        case 2:
            if i < len(GRID) - 1:
                return (i + 1, j)
        case 3:
            if j > 0:
                return (i, j - 1)
        
@lru_cache(maxsize=None)
def move_beam(i, j, direction):
    match GRID[i][j]:
        case ".":
            next_direction = [direction]
        case "\\":
            next_direction = [(direction - 1) % 4] if direction % 2 == 0 else [(direction + 1) % 4]
        case "/":
            next_direction = [(direction + 1) % 4] if direction % 2 == 0 else [(direction - 1) % 4]
        case "-":
            if direction % 2 == 0:
                next_direction = [1, 3]
            else:
                next_direction = [direction]
        case "|":
            if direction % 2 == 1:
                next_direction = [0, 2]
            else:
                next_direction = [direction]

    res = []
    for d in next_direction:
        next_pos = get_next_position(i, j, d)
        if next_pos:
            res.append((*next_pos, d))
    return res

@lru_cache(maxsize=None)
def energise_tiles(si, sj, sd):
    q = Queue()
    q.put((si, sj, sd))
    visited = set()
    while not q.empty():
        i, j, d = q.get()
        if (i, j, d) in visited:
            continue

        visited.add((i, j, d))
        movement = move_beam(i, j, d)
        
        while len(movement) == 1:
            i, j, d = movement[0]
            visited.add((i, j, d))
            movement = move_beam(i, j, d)
        
        for move in movement:
            q.put(move)

    tiles = set()
    for i, j, _ in visited:
        tiles.add((i, j))

    return len(tiles)

res = energise_tiles(0, 0, 1)
print(f"Part 1: {res}")

res = 0
for i in range(len(GRID)):
    res = max(res, energise_tiles(i, 0, 1))
    res = max(res, energise_tiles(i, len(GRID[0]) - 1, 3))
for j in range(len(GRID[0])):
    res = max(res, energise_tiles(0, j, 2))
    res = max(res, energise_tiles(len(GRID) - 1, j, 0))

print(f"Part 2: {res}")
