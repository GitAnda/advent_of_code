from aocd import data
from pathlib import Path

txtfile =  Path(__file__).parent / (Path(__file__).stem + ".txt")
if not txtfile.exists():
    with open(txtfile, 'w') as f:
        f.write(data)

with open(txtfile) as f:
    data = [sum([int(snack) for snack in elf.split("\n")]) for elf in f.read().split("\n\n")]
elfs = sorted(data, reverse=True)

print(f"Part 1: {elfs[0]}")
print(f"Part 2: {sum(elfs[0:3])}")