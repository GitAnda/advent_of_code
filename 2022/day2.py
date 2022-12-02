import input

TO_INT = {'X': 1, 'A': 1, "Y": 2, "B": 2, "Z": 3, "C": 3}
WIN = {1: 2, 2: 3, 3: 1}
LOSE = {2: 1, 3: 2, 1: 3}
    
def parse_data():
    data = input.retrieve(__file__)
    return [[TO_INT[move] for move in r.split(" ")] for r in data.split("\n")]

def points(them, me):
    if me == them:
        return 3 + me
    elif me == WIN[them]:
        return 6 + me
    else:
        return 0 + me
    
def play(them, outcome):
    if outcome == 2:
        return them
    elif outcome == 1:
        return LOSE[them]
    else:
        return WIN[them]
            
print(f"Part 1: {sum([points(t, m) for t, m in parse_data()])}")
print(f"Part 2: {sum([points(t, play(t, o)) for t, o in parse_data()])}")