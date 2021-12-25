file_name = 'day25.txt'
with open(file_name) as f:
    cucumbers = f.read().strip().split('\n')
east_cucumbers = {(i, j) for i, line in enumerate(cucumbers) for j, c in enumerate(line) if c == '>'}
south_cucumbers = {(i, j) for i, line in enumerate(cucumbers) for j, c in enumerate(line) if c == 'v'}
max_y = len(cucumbers)
max_x = len(cucumbers[0])


def step(east, south):
    new_east = set()
    new_south = set()
    move = False
    for y, x in east:
        if (y, (x + 1) % max_x) in east or (y, (x + 1) % max_x) in south:
            new_east.add((y, x))
        else:
            new_east.add((y, (x + 1) % max_x))
            move = True

    for y, x in south:
        if ((y + 1) % max_y, x) in new_east or ((y + 1) % max_y, x) in south:
            new_south.add((y, x))
        else:
            new_south.add(((y + 1) % max_y, x))
            move = True

    return move, new_east, new_south


count = 0
while True:
    move, east_cucumbers, south_cucumbers = step(east_cucumbers, south_cucumbers)
    count += 1
    if not move:
        break


print(f'Part 1: {count}')



