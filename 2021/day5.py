file_name = 'day5.txt'

with open(file_name) as f:
    lines = [[tuple([int(p) for p in c.split(',')]) for c in x.split(' -> ')] for x in f.read().strip().split('\n')]

area = {}
for line in lines:
    p1, p2 = line
    if p1[0] == p2[0]:
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            if (p1[0], y) in area.keys():
                area[(p1[0], y)] += 1
            else:
                area[(p1[0], y)] = 1
    elif p1[1] == p2[1]:
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            if (x, p1[1]) in area.keys():
                area[(x, p1[1])] += 1
            else:
                area[(x, p1[1])] = 1
    else:
        if p2[0] < p1[0]:
            p1, p2 = p2, p1
        if p1[1] > p2[1]:
            for i in range(p1[1] - p2[1] + 1):
                if (p1[0]+i, p1[1]-i) in area.keys():
                    area[(p1[0]+i, p1[1]-i)] += 1
                else:
                    area[(p1[0]+i, p1[1]-i)] = 1
        else:
            for i in range(p2[1] - p1[1] + 1):
                if (p1[0]+i, p1[1]+i) in area.keys():
                    area[(p1[0]+i, p1[1]+i)] += 1
                else:
                    area[(p1[0]+i, p1[1]+i)] = 1

count = 0
for v in area.values():
    if v > 1:
        count += 1

# print(area)

print(f'Part 1: {count}')