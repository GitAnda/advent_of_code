with open('day2.txt') as f:
    operations = [x.split() for x in f.read().strip().split('\n')]

position = 0
depth = 0

for a, n in operations:
    if a == 'forward':
        position += int(n)
    elif a == 'up':
        depth -= int(n)
    elif a == 'down':
        depth += int(n)

print(f'Part 1: {depth*position}')

position = 0
depth = 0
aim = 0

for a, n in operations:
    if a == 'forward':
        position += int(n)
        depth += aim*int(n)
    elif a == 'up':
        aim -= int(n)
    elif a == 'down':
        aim += int(n)

print(f'Part 2: {depth*position}')
