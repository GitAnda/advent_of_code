import input
    
def parse_data():
    data = input.retrieve(__file__)
    return data

elfs = sorted(parse_data(), reverse=True)

print(f"Part 1: {elfs[0]}")
print(f"Part 2: {sum(elfs[0:3])}")