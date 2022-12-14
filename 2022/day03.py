import input
    
def parse_data():
    data = input.retrieve(__file__)
    return data

def priority(char):
    if char.islower():
        return ord(char) - 97 + 1
    else:
        return ord(char) - 65 + 27
    
data = parse_data().split()
shared = [(set(d[:len(d)//2]) & set(d[len(d)//2:])).pop() for d in data]
print(f"Part 1: {sum([priority(s) for s in shared])}")

shared = [(set(data[i]) & set(data[i+1]) & set(data[i+2])).pop() for i in range(0, len(data), 3)]
print(f"Part 2: {sum([priority(s) for s in shared])}")