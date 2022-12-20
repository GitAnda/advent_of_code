import input
import regex as re
    
def parse_data():
    r = r'^Sensor at x=(.*?), y=(.*?): closest beacon is at x=(.*?), y=(.*?)$'
    data = [[(int(a), int(b)), (int(c), int(d))] for d in input.retrieve(__file__).split('\n') for a, b, c, d in re.findall(r, d)]
    return data

def get_ranges(row, distances):    
    no_set = []
    for s, d in distances.items():
        x, y = s
        dx = d - abs(row - y)
        if dx >= 0:
            no_set.append((x - dx, x + dx))
    
    new_set = []
    no_set.sort()
    
    x1, x2 = no_set[0]
    for (x3, x4) in no_set[1:]:
        if x3 <= x2 + 1:
            x2 = max(x2, x4)
        else:
            new_set.append((x1, x2))
            x1, x2 = x3, x4
            
    new_set.append((x1, x2))            
    return new_set

def get_ranges_constrained(row, distances, m):    
    no_list = []
    for s, d in distances.items():
        x, y = s
        dx = d - abs(row - y)
        if dx >= 0:
            no_list.append((x - dx, x + dx))
    
    new_set = set()
    for x1, x2 in no_list:
        if not x2 < 0 or x1 > m:
            if x1 <= 0:
                x1 = 0
            if x2 >= m:
                x2 = m
            new_set.add((x1, x2))
        
    no_list = list(new_set)
    no_list.sort()
    
    new_set = []
    x1, x2 = no_list[0]
    for (x3, x4) in no_list[1:]:
        if x3 <= x2 + 1:
            x2 = max(x2, x4)
        else:
            new_set.append((x1, x2))
            x1, x2 = x3, x4
            
    new_set.append((x1, x2))            
    return new_set

        
def find_signal(distances, m):
    for y in range(m + 1):
        # if y % 10000:
            # print(f"{round(y / m * 100)}%", end='\r')
        ranges = get_ranges_constrained(y, distances, m)
        if len(ranges) != 1:
            return (ranges[0][1] + 1) * m + y
    
    
sensors = parse_data()
distance = {s: abs(s[0] - b[0]) + abs(s[1] - b[1]) for s, b in sensors}

row_number = 2000000
no_sensor = set([s[0] for s, _ in sensors if s[1] == row_number])
no_beacon = set([b[0] for _, b in sensors if b[1] == row_number])
res = sum([x2 - x1 + 1 for x1, x2 in get_ranges(row_number, distance)]) - len(no_beacon) - len(no_sensor)
print(f"Part 1: {res}")


m = 4000000
res = find_signal(distance, m)
print(f"Part 2: {res}")
