import input
import math
    
def parse_data():
    data = [(d.split()[0], int(d.split()[1])) for d in input.retrieve(__file__).split('\n')]
    return data

data = parse_data()
# print(data)

def move(loc_head, loc_tail, direction=None):
    x, y = loc_head
    if direction == "U":
        loc_head = (x - 1, y)
    elif direction == "D":
        loc_head = (x + 1, y)
    elif direction == "L":
        loc_head = (x, y - 1)
    elif direction == "R":
        loc_head = (x, y + 1)
        
    x, y = loc_head
    a, b = loc_tail
    if abs(a - x) > 1 and abs(b - y) > 1:
        loc_tail = (x + int(math.copysign(1, a - x)), y + int(math.copysign(1, b - y)))
    elif abs(a - x) > 1:
        loc_tail = (x + int(math.copysign(1, a - x)), y)
    elif abs(b - y) > 1:
        loc_tail = (x, y + int(math.copysign(1, b - y)))
    
    assert abs(loc_head[0] - loc_tail[0]) <= 1 and abs(loc_head[1] - loc_tail[1]) <= 1, f"tail too far away! head {loc_head}, tail {loc_tail}"
    
    return loc_head, loc_tail

def move_n(positions, direction):
    head = positions[0]
    new_positions = []
    first = True
    for tail in positions[1:]:
        if first:
            h, t = move(head, tail, direction)
            first = False
        else:
            h, t = move(head, tail)
        new_positions.append(h)
        head = t
    new_positions.append(t)
    return new_positions

def track_tail(moves, n):
    pos = [(0, 0)] * n
    
    tail_pos = set()
    for d, n in moves:
        for _ in range(n):
            pos = move_n(pos, d)
            tail_pos.add(pos[-1])
            
    return tail_pos

res = len(track_tail(data , 2))
print(f"Part 1: {res}")

res = len(track_tail(data , 10))
print(f"Part 2: {res}")
