import aoc_input
import re
import math as m

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n")

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)
# data = [[d for d in dat.split(' ')] for dat in data]

def get_valid_neighbours(pos):
    i, j = pos
    char = data[i][j]

    match char:
        case "S":
            neighbours = []
            if data[i-1][j] in ("|", "7", "F"):
                neighbours.append((i-1,j))
            if data[i+1][j] in ("|", "L", "J"):
                neighbours.append((i+1,j))
            if data[i][j-1] in ("-", "L", "F"):
                neighbours.append((i,j-1))
            if data[i][j+1] in ("-", "J", "7"):
                neighbours.append((i,j+1))
            return set(neighbours)
        case "F":
            return {(i, j+1), (i+1, j)}
        case "7":
            return {(i, j-1), (i+1, j)}
        case "J":
            return {(i, j-1), (i-1, j)}
        case "L":
            return {(i, j+1), (i-1, j)}
        case "-":
            return {(i, j-1), (i, j+1)}
        case "|":
            return {(i+1, j), (i-1, j)}

visited = set(start)
count = 0
pos = start
while True:
    neighbours = get_valid_neighbours(pos)
    neighbours = neighbours.difference(visited)

    if not neighbours:
        break

    pos = neighbours.pop()
    visited.add(pos)

    count += 1

res = count // 2
print(f"Part 1: {res}")

res = 0
for i in range(len(data)):
    s = ""
    for j in range(len(data[0])):
        if (i,j) in visited:
            s += data[i][j]
        else:
            s += " "
    # print(s)

    line = s.strip().replace('-', '')
    if line:
        index = 0
        count = 0
        while index < len(line):
            char = line[index]
            match char:
                case "|":
                    count += 1
                    index += 1
                case "L":
                    if line[index+1] == "7":
                        count += 1
                    index += 2
                case "F":
                    if line[index+1] == "J":
                        count += 1
                    index += 2
                case " ":
                    if count % 2 != 0:
                        res += 1
                    index += 1
        
print(f"Part 2: {res}")    
        