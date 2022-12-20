import input
    
def parse_data():
    data = [[tuple([int(y) for y in x.split('-')]) for x in i.split(',')] for i in input.retrieve(__file__).split()]
    return data

def contains(pair1, pair2):
    x1, y1 = pair1
    x2, y2 = pair2
    if x1 <= x2 and y2 <= y1:
        return True
    return False

def overlaps(pair1, pair2):
    x1, y1 = pair1
    x2, y2 = pair2
    if y1 < x2 or y2 < x1:
        return False
    return True
    
data = parse_data()
contained = [contains(d[0], d[1]) or contains(d[1], d[0]) for d in data]
print(f"Part 1: {sum(contained)}")

overlap = [overlaps(d[0], d[1]) for d in data]
print(f"Part 2: {sum(overlap)}")