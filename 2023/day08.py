import aoc_input
import re
import math as m

day = int(__file__[-5:-3])
instr, data = aoc_input.get(day).strip().split("\n\n")

network = {}
for line in data.split("\n"):
    node, left, right = re.findall("([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)[0]
    network[node] = (left, right)

def get_new_pos(pos, LR):
    if LR == "L":
        return network[pos][0]
    return network[pos][1]

def count_to_end(pos):
    count = 0

    while True:
        if pos[2] == "Z":
            break

        index = count % len(instr)
        pos = get_new_pos(pos, instr[index])
        
        count += 1

    return count

print(f"Part 1: {count_to_end('AAA')}")

count = 0
start_nodes = [n for n in network if n[2] == 'A']
counts = [count_to_end(n) for n in start_nodes]

print(f"Part 2: {m.lcm(*counts)}")    
        