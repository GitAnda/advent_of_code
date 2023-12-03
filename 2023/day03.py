import aoc_input

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n")

def get_neighbours(data, i, j):
    neighbours = {}

    if i-1 >= 0:
        neighbours[(i-1, j)] = data[i-1][j]
    if i-1 >= 0 and j-1 >= 0:
        neighbours[(i-1, j-1)] = data[i-1][j-1]
    if i-1 >= 0 and j+1 < len(data[0]):
        neighbours[(i-1, j+1)] = data[i-1][j+1]
    if j-1 >= 0:
        neighbours[(i, j-1)] = data[i][j-1]
    if j+1 < len(data[0]):
        neighbours[(i, j+1)] = data[i][j+1]
    if i+1 < len(data) and j-1 >= 0:
        neighbours[(i+1, j-1)] = data[i+1][j-1]
    if i+1 < len(data):
        neighbours[(i+1, j)] = data[i+1][j]
    if i+1 < len(data) and j+1 < len(data[0]):
        neighbours[(i+1, j+1)] = data[i+1][j+1]

    return neighbours

def get_number(data, i, j):
    line = data[i]
    number = line[j]
    minj, maxj = 0, len(line)

    for k, char in enumerate(line[0:j][::-1]):
        if char.isnumeric():
            number = char + number
        else: 
            minj = j - k
            break
    
    for k, char in enumerate(line[j+1:]):
        if char.isnumeric():
            number += char
        else: 
            maxj = j + k
            break
    
    return int(number), minj, maxj

part_numbers = {}
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if not char.isnumeric() and not char == ".":
            neighbours = get_neighbours(data, i, j)
            for (ni, nj), nchar in neighbours.items():
                if nchar.isnumeric():
                    part, minnj, maxnj = get_number(data, ni, nj)
                    part_numbers[(ni, minnj, maxnj)] = part 

res = sum(part_numbers.values())
print(f"Part 1: {res}")

gears = {}
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "*":

            neighbours = get_neighbours(data, i, j)
            part_numbers = {}

            for (ni, nj), nchar in neighbours.items():
                if nchar.isnumeric():
                    part, minnj, maxnj = get_number(data, ni, nj)
                    part_numbers[(ni, minnj, maxnj)] = part 
            
            if len(part_numbers) == 2:
                gears[(ni, nj)] = list(part_numbers.values())

res = sum([parts[0] * parts[1] for parts in gears.values()])
print(f"Part 2: {res}")    
        