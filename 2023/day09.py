import aoc_input

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n")
data = [[int(d) for d in dat.split(' ')] for dat in data]

def diff(array):
    diff = []
    for l1, l2 in zip(array, array[1:]):
        diff.append(l2 - l1)
    return diff

def predict_next(initial_array):
    res = initial_array[-1]

    count = 0
    array = [a for a in initial_array]
    while not all([a == 0 for a in array]):
        array = diff(array)
        res += array[-1]
        count += 1

    return res

def predict_prev(initial_array):
    res = initial_array[0]

    count = 0
    array = [a for a in initial_array]
    while not all([a == 0 for a in array]):
        array = diff(array)
        if count % 2 == 0:
            res -= array[0]
        else:
            res += array[0]
        count += 1

    return res

res = sum([predict_next(d) for d in data])
print(f"Part 1: {res}")

res = sum([predict_prev(d) for d in data])
print(f"Part 2: {res}")    
        