import input
from functools import lru_cache
    
def parse_data():
    m, r = input.retrieve(__file__).split('\n\n')
    
    wall = set()
    path = set()
    for y, line in enumerate(m.split('\n')):
        for x, c in enumerate(line):
            if c == ".":
                path.add((x+1, y+1))
            elif c == "#":
                wall.add((x+1, y+1))
                
    route = eval("[" + r.replace('R', ',"R",').replace('L',',"L",') + "]")
       
    return wall, path, route

WALL, PATH, ROUTE = parse_data()
WRAP = {}
for d in range(50):
    WRAP[(3, 51 + d, 1)] = (0, 1, 151 + d)
    WRAP[(2, 1, 151 + d)] = (1, 51 + d, 1)
    
    WRAP[(2, 51, 1 + d)] = (0, 1, 150 - d)
    WRAP[(2, 1, 150 - d)] = (0, 51, 1 + d)
    
    WRAP[(2, 52, 51 + d)] = (1, 1 + d, 101)
    WRAP[(3, 1 + d, 101)] = (0, 52, 51 + d)
    
    WRAP[(3, 101 + d, 1)] = (3, 1 + d, 200)
    WRAP[(3, 1 + d, 200)] = (3, 101 + d, 1)
    
    WRAP[(0, 151, 1 + d)] = (2, 100, 150 - d)
    WRAP[(0, 100, 150 - d)] = (2, 151, 1 + d)
    
    WRAP[(1, 52 + d, 150)] = (2, 50, 151 + d)
    WRAP[(0, 50, 151 + d)] = (3, 52 + d, 150)
    
    WRAP[(1, 102 + d, 50)] = (2, 100, 51 + d)
    WRAP[(0, 100, 51 + d)] = (3, 102 + d, 50)

def wrap_pos(p, dx, dy):
    while True:
        x, y = p
        if (x - dx, y - dy) not in WALL | PATH:
            return (x, y)
        p = (x - dx, y - dy)


def walk(cube=False):
    pos = min([(x,y) for x,y in PATH if y == 1])
    face = 0

    for r in ROUTE:
        if r == 'R':
            face = (face + 1) % 4
            # print("turn right:", face)
        elif r == 'L':
            face = (face - 1) % 4
            # print("turn left:", face)
            
        else:
            for _ in range(r):
                x, y = pos
                # print("Current position", pos)
                
                if face == 0:
                    dx, dy = 1, 0
                elif face == 1:
                    dx, dy = 0, 1
                elif face == 2:
                    dx, dy = -1, 0
                elif face == 3:
                    dx, dy = 0, -1
                
                new_pos = (x + dx, y + dy)
                # print(new_pos)
                if new_pos not in PATH | WALL:
                    # print("New pos not in map!")
                    if cube:
                        face, a, b = WRAP[(face, *new_pos)]
                        new_pos = a, b
                    else:
                        new_pos = wrap_pos(new_pos, dx, dy)
                    
                    
                    # print(new_pos)
                    
                if new_pos in WALL:
                    # print("New pos is wall! Stay at", pos)
                    break
                
                pos = new_pos
                # print("Take a step to", pos)
            # print(pos)
            
    x, y = pos
    return 1000 * y + 4 * x + face  
            
# res = walk()
# print(f"Part 1: {res}")



res = walk(cube=True)
print(f"Part 2: {res}")
