import input
import queue
from functools import lru_cache
import math

def parse_data():
    data = input.retrieve(__file__).split('\n')
    blizzards = set()
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == ">":
                blizzards.add((0, (r-1, c-1)))
            elif char == "v":
                blizzards.add((1, (r-1, c-1)))
            elif char == "<":
                blizzards.add((2, (r-1, c-1)))
            elif char == "^":
                blizzards.add((3, (r-1, c-1)))
    return blizzards, (0, len(data) - 2, 0, len(data[0]) - 2)

BLIZZARDS, (MINR, MAXR, MINC, MAXC) = parse_data()
LCM = math.lcm(MAXR, MAXC)
START = (-1, 0)
END = (MAXR, MAXC - 1)
THERE, BACK = -1, 1

@lru_cache(MAXC*MAXR)
def storm(time):
    new_blizzards = set()
    for d, (row, column) in BLIZZARDS:
        if d == 0:
            new_blizzards.add((row, (column + time) % MAXC))
        elif d == 1:
            new_blizzards.add(((row + time) % MAXR, column))
        elif d == 2:
            new_blizzards.add((row, (column - time) % MAXC))
        elif d == 3:
            new_blizzards.add(((row - time) % MAXR, column))
    return new_blizzards


def move(start_time, there_and_back_again):
    if there_and_back_again == THERE:
        start_pos, end_pos = START, END
    else:
        start_pos, end_pos = END, START
        
    q = queue.PriorityQueue()
    sr, sc = start_pos
    q.put((sr * sc * there_and_back_again, start_time, *start_pos))
    states = {}
    best = float('inf')
    
    while not q.empty():
        _, t, r, c = q.get()
        
        # prune brances arriving in the same state after more time
        if (t % LCM, r, c) in states and states[(t % LCM, r, c)] <= t:
            continue
        states[(t % LCM, r, c)] = t
        
        # prune branches taking a longer time than current best
        if t + 1 >= best:
            continue
        
        bliz = storm((t + 1) % LCM)
        moves = {(r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)}
        for mov in moves:
            # stop if end is reached and update best
            if mov == end_pos:
                if t + 1 < best:
                    # print(f"new best found {t + 1}")
                    best = t + 1
                continue
            
            # allow waiting at start
            if mov == start_pos and (r, c) == start_pos:
                sr, sc = start_pos
                q.put((sr * sc * there_and_back_again, t + 1, *start_pos))
                continue
            
            # check that move is in the valley
            mr, mc = mov
            if (mr < MINR or mr >= MAXR or mc < MINC or mc >= MAXC):
                continue
            
            # update queue with allowed moves
            if not mov in bliz:
                q.put((mr * mc * there_and_back_again, t + 1, mr, mc))
                
    return best
            
                
# for t in range(20):
#     bliz = storm(t)
#     print(f"Time {t}")
#     for r in range(MAXR):
#         line = ''
#         for c in range(MAXC):
#             if (r, c) in bliz:
#                 line += '@'
#             else:
#                 line += '.'
#         print(line)
#     print()           
    

res = move(0, THERE)
print(f"Part 1: {res}")


res = move(move(res, BACK), THERE)
print(f"Part 2: {res}")


