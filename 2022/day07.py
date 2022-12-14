import input
from pathlib import Path
from functools import lru_cache

TOTAL_SIZE = 70000000
NEEDED_SIZE = 30000000
    
def parse_data():
    data = input.retrieve(__file__).split('\n')
    
    path = Path("")
    dirs = {}
    idx = 0
    while idx < len(data):
        line = data[idx]
        if line == '$ cd ..':
            path = path.parent
        elif line.startswith('$ cd'):
            path = path / Path(data[idx][5:])
        elif line == '$ ls':
            contains = []
            while idx < len(data) -  1 and not data[idx + 1].strip().startswith('$'):
                contains.append(data[idx + 1])
                idx += 1
            dirs[path] = contains
        else:
            print("Command not recognised: ", line)
            
        idx += 1 
            
    return dirs

DATA = parse_data()

@lru_cache
def calculate_size(path):
    size = 0
    for ls in DATA[path]:
        if ls.startswith('dir'):
            size += calculate_size(path / ls[4:])
        else:
            size += int(ls.split()[0])     
        
    return size

sizes = {str(path): calculate_size(path) for path in DATA}
res = sum([size for size in sizes.values() if size <= 100000])
print(f"Part 1: {res}")

used_size = sizes['\\']
res = min([size for size in sizes.values() if used_size - size < TOTAL_SIZE - NEEDED_SIZE])
print(f"Part 2: {res}")