import aoc_input
import re
import math as m

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n")

double_row = set()
double_col = set()
galaxies = set()

for i, line in enumerate(data):
    if len(set(line)) == 1:
        double_row.add(i)
    
    for j, char in enumerate(line):
        if char == "#":
            double_col.add(j)
            galaxies.add((i, j))

double_col = set(range(len(data[0]))).difference(double_col)

res1 = 0
res2 = 0
for i1, j1 in galaxies:
    for i2, j2 in galaxies:
        h = abs(i1 - i2)
        w = abs(j1 - j2)

        ch = sum([c in range(min(i1, i2), max(i1, i2)) for c in double_row])
        cw = sum([c in range(min(j1, j2), max(j1, j2)) for c in double_col])

        res1 += h + w + ch + cw
        res2 += h + w + (ch + cw)*(1000000 - 1)

print(f"Part 1: {res1 // 2}")

res = 0    
print(f"Part 2: {res2 // 2}")    
