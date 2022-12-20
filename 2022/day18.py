import input
import queue
    
def parse_data():
    data = [tuple([int(x) for x in d.split(',')]) for d in input.retrieve(__file__).split('\n')]
    return set(data)

DATA = parse_data()
SIDES = {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)}
x, y, z = ([pos[0] for pos in DATA], [pos[1] for pos in DATA], [pos[2] for pos in DATA])
MINMAX = ((min(x)-1, max(x)+1), (min(y)-1, max(y)+1), (min(z)-1, max(z)+1))

def surface_area():
    surface = 0
    for x, y, z in DATA:
        for i, j, k in SIDES:
            if not (x+i, y+j, z+k) in DATA:
                surface += 1
                
    return surface


def external_surface_area():
    q = queue.Queue()
    q.put((-1, -1, -1))
    external = set()
    surface = 0
    
    while not q.empty():
        pos = q.get()
        x, y, z = pos
        if x < MINMAX[0][0] or x > MINMAX[0][1] or y < MINMAX[1][0] or y > MINMAX[1][1] or z < MINMAX[2][0] or z > MINMAX[2][1]:
            continue
        
        external.add(pos)
        
        for i, j, k in SIDES:
            n = (x+i, y+j, z+k)
            if not n in external and not n in q.queue:
                if not n in DATA:
                    q.put(n)
                else:
                    surface += 1
    
    return surface
    

res = surface_area()
print(f"Part 1: {res}")

res = external_surface_area()
print(f"Part 2: {res}")

