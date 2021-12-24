initial_pos1, score1 = 6, 0
initial_pos2, score2 = 3, 0

# initial_pos1, score1 = 4, 0
# initial_pos2, score2 = 8, 0

dice_values = [1, 2, 3]
die_loops = 0

def increase_dice(dice, loops):
    if 96 <= dice[0] <= 98:
        loops += 1
    return [(x + 3 - 1) % 100 + 1 for x in dice], loops

pos1, pos2 = initial_pos1, initial_pos2
while True:
    pos1 = (pos1 + sum(dice_values) - 1)%10 + 1
    score1 += pos1
    if score1 >= 1000:
        print(f'Part 1: {(die_loops * 100 + dice_values[-1]) * score2}')
        break
    dice_values, die_loops = increase_dice(dice_values, die_loops)

    pos2 = (pos2 + sum(dice_values)) % 10
    score2 += pos2
    if score2 >= 1000:
        print(f'Part 1: {(die_loops * 100 + dice_values[-1]) * score1}')
        break
    dice_values, die_loops = increase_dice(dice_values, die_loops)


wins = [0, 0]
sum_of_dice = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
game_states = {(1, (initial_pos1, 0), (initial_pos2, 0)): 1}
while game_states:
    new_game_states = {}
    for key, dimensions in game_states.items():
        turn, player1, player2 = key
        if turn == 1:
            pos, score = player1
        else:
            pos, score = player2

        for d, n in sum_of_dice.items():
            new_pos = (pos + d - 1) % 10 + 1
            new_score = score + new_pos
            if new_score >= 21:
                wins[turn - 1] += dimensions * n
            else:
                if turn == 1:
                    new_game_state = (2, (new_pos, new_score), player2)
                else:
                    new_game_state = (1, player1, (new_pos, new_score))

                if new_game_state in new_game_states.keys():
                    new_game_states[new_game_state] += n * dimensions
                else:
                    new_game_states[new_game_state] = n * dimensions

    game_states = new_game_states

# print(wins)
print(f'Part 2: {max(wins)}')
