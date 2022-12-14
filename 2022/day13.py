import input
from functools import cmp_to_key
    
def parse_data():
    data = [[eval(x) for x in d.split('\n')] for d in input.retrieve(__file__).split('\n\n')]
    return data

data = parse_data()

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0
    else:
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]
            
        for i in range(len(left)):
            lefti = left[i]
            try:
                righti = right[i]
            except IndexError:
                return -1
            
            c = compare(lefti, righti)
            if c != 0:
                return c
            
        if len(left) < len(right):
            return 1
        
        return 0

res = sum([i+1 for i, x in enumerate([compare(left, right) for left, right in data]) if x == 1])
print(f"Part 1: {res}")

data = [x for d in parse_data() for x in d] + [[[2]], [[6]]]
sorted_data = sorted(data, key=cmp_to_key(compare), reverse=True)
res = (sorted_data.index([[2]]) + 1) * (sorted_data.index([[6]]) + 1)
print(f"Part 2: {res}")
