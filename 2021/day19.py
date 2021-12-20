import queue

file_name = 'day19.txt'
with open(file_name) as f:
    scanners = {i: [[int(x) for x in beacon.split(',')] for beacon in scanner.split('\n')[1:]] for i, scanner in
                enumerate(f.read().strip().split('\n\n'))}


def are_overlapping_beacons(scanner1, scanner2):
    for beacon1 in scanner1:
        for beacon2 in scanner2:
            d = [x1 - x2 for x1, x2 in zip(beacon1, beacon2)]
            count = 0
            for b2 in scanner2:
                if [x1 + x2 for x1, x2 in zip(b2, d)] in scanner1:
                    count += 1
                if count >= 12:
                    return True, d
    return False, None


def rotate_scanner(scanner, rx, ry, rz):
    return [rotate_vector(beacon, rx, ry, rz) for beacon in scanner]


def rotate_vector(v, rx, ry, rz):
    x, y, z = v
    for _ in range(rx):
        y, z = -z, y
    for _ in range(ry):
        x, z = -z, x
    for _ in range(rz):
        x, y = -y, x
    return [x, y, z]


def get_rotations():
    res = []
    for rx in range(4):
        for ry in range(4):
            for rz in range(4):
                res.append([rx, ry, rz])
    return res


rotations = get_rotations()
full_map = set([tuple(s) for s in scanners[0]])
distance_to_scanner0 = {0: [0, 0, 0]}
rotation_of_scanner = {0: [0, 0, 0]}
known_scanners = {0: scanners[0]}
q = queue.Queue()
q.put(0)
while not q.empty():
    i = q.get()
    scanner1 = known_scanners[i]
    for j, scanner2 in scanners.items():
        print(f'Consider scanner {i} and scanner {j}     ', end='\r')
        for rx, ry, rz in rotations:
            rotated_scanner = rotate_scanner(scanner2, rx, ry, rz)
            if j not in known_scanners:
                b, d2 = are_overlapping_beacons(scanner1, rotated_scanner)
                if b:
                    d1 = distance_to_scanner0[i]
                    known_scanners[j] = rotated_scanner
                    rotation_of_scanner[j] = [rx, ry, rz]
                    distance_to_scanner0[j] = [x1 - x2 for x1, x2 in zip(d1, d2)]
                    print(f'Found location of scanner {j}                           ')
                    for beacon in rotated_scanner:
                        full_map.add(tuple([x1 - x2 for x1, x2 in zip(beacon, distance_to_scanner0[j])]))
                    q.put(j)
                    break


print(f'Part 1: {len(full_map)}                                  ')

max_dist = 0
for i, loc1 in distance_to_scanner0.items():
    for j, loc2 in distance_to_scanner0.items():
        if i > j:
            manhattan_dist = sum([abs(x1 - x2) for x1, x2 in zip(loc1, loc2)])
            if manhattan_dist > max_dist:
                max_dist = manhattan_dist
print(f'Part 2: {max_dist}')
