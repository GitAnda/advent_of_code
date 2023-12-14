import aoc_input
import re
from functools import lru_cache

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n\n")
patterns = [d.split("\n") for d in data]

def horizontal_reflection(pattern):
    for i in range(len(pattern) - 1):
        n = min(i+1, len(pattern)-i-1)
        for j in range(n):
            if pattern[i-j] != pattern[i+1+j]:
                break
        else:
            return i+1
        
    return 0

def horizontal_smudge(pattern):
    for i in range(len(pattern) - 1):
        n = min(i+1, len(pattern)-i-1)
        count = 0
        for j in range(n):
            count += sum(1 for a, b in zip(pattern[i-j], pattern[i+1+j]) if a != b)
            if count > 1:
                break

        if count == 1:
            return i+1
        
    return 0

def transpose(pattern):
    return [''.join(p) for p in zip(*pattern)]

res = 0
for pattern in patterns:
    res += 100 * horizontal_reflection(pattern)
    res += horizontal_reflection(transpose(pattern))
print(f"Part 1: {res}")

res = 0
for pattern in patterns:
    res += 100 * horizontal_smudge(pattern)
    res += horizontal_smudge(transpose(pattern))
print(f"Part 2: {res}")

