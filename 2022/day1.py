import input
    
def parse_data():
    data = input.retrieve(__file__)
    return [sum([int(snack) for snack in elf.split("\n")]) for elf in data.split("\n\n")]

elfs = sorted(parse_data(), reverse=True)

print(f"Part 1: {elfs[0]}")
print(f"Part 2: {sum(elfs[0:3])}")