import aoc_input

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n")

cubes = {"green": 13, "red": 12, "blue": 14}

def is_game_possible(sets):
    for s in sets:
        draws = s.split(", ")
        for draw in draws:
            num, colour = draw.split(" ")
            if cubes[colour] < int(num):
                return False
    return True

possible = []
for line in data:
    game, sets = line.split(": ")
    game = int(game.split(" ")[1])
    sets = sets.split("; ")
    if is_game_possible(sets):
        possible.append(game)

res = sum(possible)
print(f"Part 1: {res}")

def get_min_set(sets):
    min_set = {"green": 0, "red": 0, "blue": 0}
    for s in sets:
        draws = s.split(", ")
        for draw in draws:
            num, colour = draw.split(" ")
            if min_set[colour] < int(num):
                min_set[colour] = int(num)
    return min_set

powers = 0
for line in data:
    game, sets = line.split(": ")
    game = int(game.split(" ")[1])
    sets = sets.split("; ")
    min_set = get_min_set(sets)
    power = min_set["green"] * min_set["red"] * min_set["blue"]
    powers += power


res = powers
print(f"Part 2: {res}")    
        