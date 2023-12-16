import aoc_input
from functools import lru_cache
from tqdm import tqdm

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split(",")

def hash(string):
    value = 0
    for char in string:
        value = ((value + ord(char)) * 17) % 256
    return value

res = 0
for line in data:
    res += hash(line)
print(f"Part 1: {res}")


boxes = {box: [] for box in range(256)}
for line in data:
    if line[-1] == "-":
        label = line[:-1]
        box = hash(label)
        lenses = boxes[box]

        for i, (lens_label, lens_value) in enumerate(lenses):
            if lens_label == label:
                boxes[box] = lenses[:i] + lenses[i+1:]
                break
    else:
        label, value = line.split("=")
        value = int(value)

        box = hash(label)
        lenses = boxes[box]
        for i, (lens_label, lens_value) in enumerate(lenses):
            if lens_label == label:
                boxes[box][i][1] = value
                break
        else:
            boxes[box].append([label, value])

res = 0
for box, lenses in boxes.items():
    for i, (_, value) in enumerate(lenses):
        res += (box + 1) * (i + 1) * value
print(f"Part 2: {res}")

