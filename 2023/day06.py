import aoc_input
import re
import numpy as np
import math as m

day = int(__file__[-5:-3])
time, dist = aoc_input.get(day).strip().split("\n")
time = [int(r) for r in re.findall("\d+", time)]
dist = [int(r) for r in re.findall("\d+", dist)]

def win_margin(time, dist):
    res = 0
    for t in range(time + 1):
        if t * (time - t) > dist:
            res += 1
    return res

beats = 1
for t, d in zip(time, dist):
    beats *= win_margin(t, d)

print(f"Part 1: {beats}")

time, dist = aoc_input.get(day).strip().split("\n")
time = int("".join(re.findall("\d+", time)))
dist = int("".join(re.findall("\d+", dist)))

lower = m.ceil(0.5 * time - np.sqrt(0.25*(time**2) - dist))
upper = int(0.5 * time + np.sqrt(0.25*(time**2) - dist))

res = upper - lower + 1
print(f"Part 2: {res}")    
        