import input
    
def parse_data():
    return [int(x) for x in input.retrieve(__file__).split('\n')]
    
def mix(l):
    N = len(l)
    for og_idx in range(N):
        
        for idx in range(N):
            v, i = l[idx]
            if i == og_idx:
                break

        r = (idx + v) % (N - 1)
        if r > idx:
            l = l[:idx] + l[idx+1:r+1] + [(v, i)] + l[r+1:]
        if idx > r:
            l = l[:r] + [(v, i)] + l[r:idx] + l[idx+1:]
        if idx == r:
            l = l[:idx] + [(v, i)] + l[idx+1:]
    
    return l

def calc_coord(l):
    idx = 0 
    N = len(l)
    while True:
        v, _ = l[idx]
        if v == 0:
            break
        idx += 1
        
    return l[(idx+1000)%N][0] + l[(idx+2000)%N][0] + l[(idx+3000)%N][0]
  
data = [(v, i) for i, v in enumerate(parse_data())]
res = calc_coord(mix(data))
print(f"Part 1: {res}")

KEY = 811589153
data = [(v * KEY, i) for i, v in enumerate(parse_data())]
for _ in range(10):
    data = mix(data)
res = calc_coord(data)
print(f"Part 2: {res}")
