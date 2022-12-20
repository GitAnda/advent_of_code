import input
    
def parse_data():
    data = [1 if c == ">" else -1 for c in input.retrieve(__file__)]
    return data

JETS = parse_data()
ROCKS = [((4, 1), {(0, 0), (1, 0), (2, 0), (3, 0)}),
         ((3, 3), {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)}),
         ((3, 3), {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}),
         ((1, 4), {(0, 0), (0, 1), (0, 2), (0, 3)}),
         ((2, 2), {(0, 0), (1, 0), (0, 1), (1, 1)})]

def get_rock(a, b, shape):
    return {(a + xi, b + yi) for xi, yi in shape}
            
            
max_height = 0
jet_count = 0
tower = {(0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1)}
res = {}
heigh_to_rocks = {}
N = 2*2022

for n in range(N + 1):        
    x, y = (2, max_height + 3)
    (w, h), rock = ROCKS[n % len(ROCKS)]
    
    while True:
        jet = JETS[jet_count % len(JETS)]
        jet_count += 1
        
        new_x = max(0, min(7 - w, x + jet))
        if not tower.intersection(get_rock(new_x, y, rock)):
            x = new_x

        new_y = y - 1
        if tower.intersection(get_rock(x, new_y, rock)):
            tower = tower.union(get_rock(x, y, rock))
            max_height = max(max_height, y + h)
            break
        
        y = new_y
    
    heigh_to_rocks[max_height] = n
    res[n + 1] = max_height
    

print(f"Part 1: {res[2022]}")


match_pattern = {(x, y - max_height + 10) for x, y in tower if y >= max_height - 10}
for height in range(max_height - 10, 0, -1):
    current_pattern = {(x, y - height + 10) for x, y in tower if y >= height - 10 and y < height}
    if current_pattern == match_pattern:
        LOOP_HEIGHT = max_height - height
        LOOP_ROCKS = heigh_to_rocks[max_height] - heigh_to_rocks[height]
        break


loops, rocks = divmod(1000000000000, LOOP_ROCKS)
print(f"Part 2: {LOOP_HEIGHT * loops + res[rocks]}")


