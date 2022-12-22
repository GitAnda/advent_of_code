import input

# x = open("2022/day22.txt", "r").read()
# grid, ins = x.split("\n\n")

def parse_data():
    m, r = input.retrieve(__file__).split('\n\n')
    # m, r = open("2022\day22.txt").read().split("\n\n")
    
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
    (fa, xa, ya), (fb, xb, yb) = (3, 51, 1), (0, 1, 151)
    WRAP[(fa, xa+d, ya)] = (fb, xb, yb+d)
    WRAP[((fb-2)%4, xb, yb+d)]= ((fa-2)%4, xa+d, ya)

    (fa, xa, ya), (fb, xb, yb) = (3, 101, 1), (3, 1, 200)
    WRAP[(fa, xa+d, ya)] = (fb, xb+d, yb)
    WRAP[((fb-2)%4, xb+d, yb)]= ((fa-2)%4, xa+d, ya)

    (fa, xa, ya), (fb, xb, yb) = (1, 51, 150), (2, 50, 151)
    WRAP[(fa, xa+d, ya)] = (fb, xb, yb+d)
    WRAP[((fb-2)%4, xb, yb+d)]= ((fa-2)%4, xa+d, ya)

    (fa, xa, ya), (fb, xb, yb) = (2, 51, 100), (1, 50, 101)
    WRAP[(fa, xa, ya-d)] = (fb, xb-d, yb)
    WRAP[((fb-2)%4, xb-d, yb)]= ((fa-2)%4, xa, ya-d)

    (fa, xa, ya), (fb, xb, yb) = (1, 101, 50), (2, 100, 51)
    WRAP[(fa, xa+d, ya)] = (fb, xb, yb+d)
    WRAP[((fb-2)%4, xb, yb+d)]= ((fa-2)%4, xa+d, ya)

    (fa, xa, ya), (fb, xb, yb) = (2, 51, 1), (0, 1, 150)
    WRAP[(fa, xa, ya+d)] = (fb, xb, yb-d)
    WRAP[((fb-2)%4, xb, yb-d)]= ((fa-2)%4, xa, ya+d)

    (fa, xa, ya), (fb, xb, yb) = (0, 150, 1), (2, 100, 150)
    WRAP[(fa, xa, ya+d)] = (fb, xb, yb-d)
    WRAP[((fb-2)%4, xb, yb-d)]= ((fa-2)%4, xa, ya+d)

def wrap_pos(p, dx, dy):
    while True:
        x, y = p
        if (x - dx, y - dy) not in WALL | PATH:
            return (x, y)
        p = (x - dx, y - dy)

def get_dxy(f):
    if f == 0:
        return 1, 0
    elif f == 1:
        return 0, 1
    elif f == 2:
        return -1, 0
    elif f == 3:
        return 0, -1

def next_pos(r, face, x, y, cube):
    if r == 'R':
        face = (face + 1) % 4
    elif r == 'L':
        face = (face - 1) % 4
    else:
        
        for _ in range(r):
            dx, dy = get_dxy(face)
            
            new_pos = (x + dx, y + dy)
            nf = face
            if new_pos not in PATH | WALL:
                if cube:
                    nf, nx, ny = WRAP[(face, x, y)]
                    new_pos = nx, ny
                else:
                    new_pos = wrap_pos(new_pos, dx, dy)
                
            if new_pos in WALL:
                break
            
            x, y = new_pos
            face = nf

    return face, x, y

def walk(cube=False):
    x, y = min([(x,y) for x,y in PATH if y == 1])
    face = 0

    for r in ROUTE:
        face, x, y = next_pos(r, face, x, y, cube)
            
    return 1000 * y + 4 * x + face 

            
res = walk()
print(f"Part 1: {res}")

res = walk(cube=True)
print(f"Part 2: {res}")


