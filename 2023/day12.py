import aoc_input
import re
from functools import lru_cache

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n")

@lru_cache(maxsize=None)
def count_arrangement(spring, counts):
    spring = spring.strip(".")
    min_len = sum(counts) + len(counts) - 1
    if len(spring) < min_len:
        return 0
    
    if len(counts) == 1:
        c = counts[0]
        options = len(spring) - c + 1
        res = 0
        for i in range(options):
            if "." in spring[i:i+c]:
                continue
            if "#" in spring[:i] + spring[i+c:]:
                continue
            res += 1
        return res

    num_cuts = len(spring) - min_len + 1
    c = counts[0]
    res = 0
    for i in range(c, c + num_cuts):
        if not spring[i] == "#" and not "#" in spring[:i-c]:
            res += count_arrangement(spring[i-c:i], (c,)) * count_arrangement(spring[i+1:], tuple(counts[1:]))
    
    return res

res = 0
for line in data:
    springs, counts = line.split(" ")
    springs = re.sub(r"(\.)(?=\1+)", "", springs.strip("."))
    counts = [int(d) for d in counts.split(",")]
    r = count_arrangement(springs, tuple(counts))
    res += r

print(f"Part 1: {res}")

res = 0
for line in data:
    springs, counts = line.split(" ")
    five_springs = re.sub(r"(\.)(?=\1+)", "", "?".join([springs] * 5).strip("."))
    counts = [int(d) for d in counts.split(",")]
    r = count_arrangement(five_springs, tuple(counts)*5)
    res += r

print(f"Part 2: {res}")

