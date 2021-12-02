with open('day1.txt') as f:
    depths = [int(x) for x in f.read().strip().split()]

N = 3
window_depths = [sum(depths[i:i+N]) for i in range(len(depths)-N+1)]

def get_increases(d):
    res = 0
    for i in range(len(d)-1):
        if d[i] < d[i+1]:
            res += 1
    return res

print(f'Part 1: {get_increases(depths)}')
print(f'Part 2: {get_increases(window_depths)}')

