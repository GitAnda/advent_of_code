import input
    
def parse_data():
    data = input.retrieve(__file__)
    return data

data = parse_data()
def find_marker(data, n):
    for i in range(len(data) - n):
        if len(set(data[i:i+n])) == n:
            return i + n

res = find_marker(data, 4)
print(f"Part 1: {res}")

res = find_marker(data, 14)
print(f"Part 2: {res}")