import aoc_input
import re
from functools import lru_cache
from tqdm import tqdm

day = int(__file__[-5:-3])
data = tuple(aoc_input.get(day).strip().split("\n"))

@lru_cache(maxsize=None)
def tilt(pattern):
    new_pattern = []
    for line in pattern:
        count_r, count_e, rock = 0, 0, 0
        rocks = []
        for i, char in enumerate(line):
            if char == "#":
                rocks.append((rock, count_r, count_e))
                count_e, count_r = 0, 0
                rock = i
            elif char == "O":
                count_r += 1
            else:
                count_e += 1
        rocks.append((rock, count_r, count_e))
            
        new_line = ""
        for rock, count_r, count_e in rocks:
            new_line += "#" + "O"*count_r + "."*count_e 

        new_pattern.append(new_line[1:])

    return tuple(new_pattern)

@lru_cache(maxsize=None)
def transpose(pattern):
    return tuple([''.join(p) for p in zip(*pattern)])

@lru_cache(maxsize=None)
def reverse(pattern):
    return tuple([reversed(line) for line in pattern])

def calculate_load(pattern):
    res = 0
    for i, line in enumerate(pattern):
        res += line.count("O") * (len(pattern) - i)
    return res

@lru_cache(maxsize=None)
def cycle(pattern):
    new_pattern = transpose(tilt(transpose(pattern)))
    new_pattern = tilt(new_pattern)
    new_pattern = transpose(reverse(tilt(reverse(transpose(new_pattern)))))
    return reverse(tilt(reverse(new_pattern)))

tilted_pattern = transpose(tilt(transpose(data)))
for line in tilted_pattern:
    print(line)
res = calculate_load(tilted_pattern)
print(f"Part 1: {res}")

pattern = data
for _ in tqdm(range(1000000000)):
    pattern = cycle(pattern)
res = calculate_load(pattern)
print(f"Part 2: {res}")

