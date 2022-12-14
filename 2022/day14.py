import input
import queue
    
def parse_data():
    data = [[tuple([int(number) for number in pair.split(',')]) for pair in line.split('-> ')] for line in input.retrieve(__file__).split('\n')]
    return data

def get_rock_set():
    data = parse_data()
    rocks = set()
    for line in data:
        for (x1, y1), (x2, y2) in zip(line, line[1:]):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    rocks.add((x1, y))
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    rocks.add((x, y1))
    return rocks          

def get_end(rocks):
    end = 0
    for _, y in rocks:
        if y > end:
            end = y
    return end  

def find_rest(rocks):
    q = queue.LifoQueue()
    q.put((500, 0))
    sand = set()
    end = get_end(rocks)  
    
    while True:
        x, y = q.get()
        if y >= end:
            break 
        
        if (x, y + 1) not in rocks | sand:
            q.put((x, y))
            q.put((x, y + 1))
        elif (x - 1, y + 1) not in rocks | sand:
            q.put((x, y))
            q.put((x - 1, y + 1))
        elif (x + 1, y + 1) not in rocks | sand:
            q.put((x, y))
            q.put((x + 1, y + 1))
        else:
            sand.add((x, y))
    
    return len(sand)

def find_rest_with_floor(rocks):
    q = queue.LifoQueue()
    q.put((500, 0))
    sand = set()
    floor = get_end(rocks) + 2
    
    while True:
        x, y = q.get()
       
        if y + 1 == floor:
            sand.add((x, y)) 
        elif (x, y + 1) not in rocks | sand:
            q.put((x, y))
            q.put((x, y + 1))
        elif (x - 1, y + 1) not in rocks | sand:
            q.put((x, y))
            q.put((x - 1, y + 1))
        elif (x + 1, y + 1) not in rocks | sand:
            q.put((x, y))
            q.put((x + 1, y + 1))
        else:
            sand.add((x, y))
            if (x, y) == (500, 0):
                break
    
    return len(sand)                

rocks = get_rock_set()
res = find_rest(rocks)
print(f"Part 1: {res}")

rocks = get_rock_set()
res = find_rest_with_floor(rocks)
print(f"Part 2: {res}")
