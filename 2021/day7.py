file_name = 'day7.txt'

with open(file_name) as f:
    positions = [int(x) for x in f.read().strip().split(',')]

# positions = [int(x) for x in '16,1,2,0,4,2,7,1,2,14'.split(',')]


# guess = int(sum(positions)/len(positions))

def calculate_fuel(pos, x):
    return sum([abs(x-p) for p in pos])

def get_min_fuel(pos, f):
    positions.sort()
    mid = len(positions) // 2
    start_guess = int((positions[mid] + positions[~mid]) / 2)
    start_fuel = f(positions, start_guess)

    d = 1
    guess = start_guess
    fuel = start_fuel
    while True:
        new_fuel = f(positions, guess+d)
        if new_fuel < fuel:
            fuel = new_fuel
            guess += 1
        else:
            break
    up_fuel = fuel

    guess = start_guess
    fuel = start_fuel
    while True:
        new_fuel = f(positions, guess-d)
        if new_fuel < fuel:
            fuel = new_fuel
            guess -= 1
        else:
            break
    down_fuel = fuel

    if down_fuel < up_fuel:
        return down_fuel
    else:
        return up_fuel

print(f'Part 1: {get_min_fuel(positions, calculate_fuel)}')

def calculate_fuel_crab(pos, x):
    return sum([sum(range(abs((x-p))+1)) for p in pos])

print(f'Part 1: {get_min_fuel(positions, calculate_fuel_crab)}')



