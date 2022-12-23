import input

def parse_data():
    data = input.retrieve(__file__).split('\n')
    locations = set()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "#":
                locations.add((x, y))
    return locations

data = parse_data()

def get_directions(x, y, n):
    dirs = [((x-1, y-1), (x, y-1), (x+1, y-1)), ((x-1, y+1), (x, y+1), (x+1, y+1)), ((x-1, y-1), (x-1, y), (x-1, y+1)), ((x+1, y-1), (x+1, y), (x+1, y+1))]
    return dirs[n%4:] + dirs[:n%4]

def get_neighbours(x, y):
    return {(x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1)}

def round(locations, n):
    # first half of the round
    proposed = {}
    for elf in locations:
        neighbours = get_neighbours(*elf)
        if not any([n in locations for n in neighbours]):
            # print(f"Elf {elf} will not move because it has no neighbours in {neighbours}")
            proposed[elf] = [elf]
            continue
            
        directions = get_directions(*elf, n)
        for direction in directions:
            if not any([d in locations for d in direction]):
                # print(f"Elf {elf} proposes {direction[1]}")
                if direction[1] in proposed:
                    proposed[direction[1]].append(elf)
                else:
                    proposed[direction[1]] = [elf]
                break
            # print(f"Elf {elf} cannot move to {direction} because there is an elf there")
        else:
            proposed[elf] = [elf]
            # print(f"Elf {elf} will not move because it has no options")
            
    # second half of the round
    new_locations = set()
    moved_elfs = 0
    for prop, elfs in proposed.items():
        if len(elfs) > 1:
            for elf in elfs:
                new_locations.add(elf)
        else:
            if prop != elfs[0]:
                moved_elfs += 1
            new_locations.add(prop)
            
    return moved_elfs, new_locations
                
def do_rounds(locations):
    
    n = 0
    an_elf_moved = 1
    while an_elf_moved:
        # print(f"Round {n}: {an_elf_moved}")
                
        an_elf_moved, locations = round(locations, n)
        
        minx = min([x for x, _ in locations])
        maxx = max([x for x, _ in locations])
        miny = min([y for _, y in locations])
        maxy = max([y for _, y in locations])
        
        if n == 9:
            print(f"Part 1: {(maxx - minx + 1) * (maxy - miny + 1) - len(locations)}")
            
        n += 1
    
    return n

res = do_rounds(data)
print(f"Part 2: {res}")


